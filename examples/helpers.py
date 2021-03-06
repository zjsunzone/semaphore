'''
    copyright 2018 to the Semaphore Authors

    This file is part of Semaphore.

    Semaphore is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Semaphore is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Semaphore.  If not, see <https://www.gnu.org/licenses/>.
'''



import sys
sys.path.insert(0, '../snarkWrapper')

import utils
from deploy import genSalt


def initMerkleTree(i):
    nullifiers = []
    sks = []
    leaves = []
    for j in range (0,i):
        nullifiers.append("0x" + genSalt(64))
        sks.append("0x" + genSalt(64))
        leaves.append(utils.hashPadded(nullifiers[j], sks[j]))
    return(leaves, nullifiers, sks)
