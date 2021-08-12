from collections import namedtuple
from heapq import heappop, heappush

people = list()
file = open("Personer.dta")
person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])


def readfile():
    for s in file.readlines():
        a, b, c, d, e = s.strip().split(";")
        people.append(person(a, b, c, d, e))


def print_lastfive():
    i = 0
    while i < 5:
        i += 1
        print(people.pop(len(people) - i))


def find_adresscount():
    listofpostnr = list()
    for p in people:
        if p.postnummer not in listofpostnr:
            listofpostnr.append(p.postnummer)
    print(len(listofpostnr))


def find_commonlastname():
    lastnames = []
    listoflastnames = []
    commonnumber = 0
    commonname = ""
    for p in people:
        lastnames.append(p.etternavn)
        if p.etternavn not in listoflastnames:
            listoflastnames.append(p.etternavn)

    for l in listoflastnames:
        currentname = listoflastnames.pop(1)
        if lastnames.count(currentname) > commonnumber:
            commonnumber = lastnames.count(currentname)
            commonname = currentname

    print(commonname, commonnumber)


def find_tencommon():
    lastnames = []
    name_counter = {}
    for p in people:
        lastnames.append(p.etternavn)

    for name in lastnames:
        if name in name_counter:
            name_counter[name] += 1

        else:
            name_counter[name] = 1

    common_names = sorted(name_counter, key=name_counter.get, reverse=True)
    print(common_names[:10])


def heap_sort_range(elements, start, stop):
    heap = []
    for i in elements:
        heappush(heap, i)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    count = start
    while count < stop:
        count += 1
        print(ordered.pop(start), count)


def heap_sort_item(elements, item):
    heapList = []
    for e in elements:
        heappush(heapList, e)
    ordered = []
    while heapList:
        ordered.append(heappop(heapList))

    print(ordered.pop(item))


def heap(elements, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and elements[i] < elements[l]:
        max = l
    if r < n and elements[max] < elements[r]:
        max = r
    if max != i:
        elements[i], elements[max] = elements[max], elements[i]  # swap
        heap(elements, n, max)


def heapSort_noLib(elements):
    n = len(elements)

    for i in range(n // 2 - 1, -1, -1):
        heap(elements, n, i)

    for i in range(n - 1, 0, -1):
        elements[i], elements[0] = elements[0], elements[i]
        heap(elements, i, 0)


readfile()

print("[Unsorted].")
print(people.pop(0))
print(people.pop(20000))
print(people.pop(40000))
print(people.pop(60000))
print(people.pop(80000))
heapSort_noLib(people)
print("\n", "[Sorted]")
print(people.pop(0))
print(people.pop(20000))
print(people.pop(40000))
print(people.pop(60000))
print(people.pop(80000))



# heap_sort_range(people, 0, 20000)
# heap_sort_range(people, 20000, 40000)
# heap_sort_range(people, 40000, 60000)
# heap_sort_range(people, 60000, 80000)


print("\n", ["Sorted"])
heap_sort_item(people, 0)
heap_sort_item(people, 20000)
heap_sort_item(people, 40000)
heap_sort_item(people, 60000)
heap_sort_item(people, 80000)

