class RankingList(object):
    def __init__(self, rank, wrapper=None):
        self._rank = rank
        self._wrapper = wrapper

    def __getitem__(self, k):
        if isinstance(k, slice):
            start = k.start if k.start else 0
            end = k.stop - 1 if k.stop else self.__len__() - 1
            step = k.step

            unique_ids = self._rank.get_range(start, end)
            if step:
                unique_ids = unique_ids[::step]

            return [self._wrap(unique_id) for unique_id in unique_ids]
        else:
            if self.__len__() <= k:
                raise IndexError('list index out of range')
            unique_ids = self._rank.get_range(k, k)
            return self._wrap(unique_ids[0])

    def _wrap(self, unique_id):
        return self._wrapper(unique_id) if self._wrapper else unique_id

    def __len__(self):
        return self._rank.get_count()
