<template>
  <nav class="pagination-container">
    <ul class="pagination">
      <li :class="['prev', { disabled: page === 1 }]" :disabled="page === 1">
        <a
          href="#"
          class="icon icon-arrow--warning"
          aria-label="Previous"
          @click="pageChange($event, page - 1)"
        >
          <span aria-hidden="true">&nbsp;</span>
        </a>
      </li>
      <li
        v-for="pageNum in pagesDisplay"
        :key="pageNum"
        :class="{ active: pageNum === page }"
      >
        <span v-if="pageNum < 0" class="separator">...</span>
        <a v-else href="#" @click="pageChange($event, pageNum)">{{
          pageNum
        }}</a>
      </li>
      <li
        :class="['next', { disabled: page >= pages }]"
        :disabled="page >= pages"
      >
        <a
          href="#"
          class="icon icon-arrow--warning"
          aria-label="Next"
          @click="pageChange($event, page + 1)"
        >
          <span aria-hidden="true">&nbsp;</span>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script>
import { range } from 'lodash';

export default {
  name: 'Pagination',
  props: {
    page: {
      type: Number,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
    perPage: {
      type: Number,
      default: 150,
    },
  },
  computed: {
    pages() {
      return Math.ceil(this.count / this.perPage);
    },
    pagesRange() {
      return range(1, this.pages + 1);
    },
    pagesDisplay() {
      if (this.pages <= 7) {
        return this.pagesRange;
      }
      if (this.page <= 4) {
        return this.pagesRange
          .slice(0, 5)
          .concat([-1])
          .concat(this.pagesRange.slice(-1));
      }
      if (this.pages - this.page < 4) {
        return this.pagesRange
          .slice(0, 1)
          .concat([-1])
          .concat(this.pagesRange.slice(-5));
      }
      return this.pagesRange
        .slice(0, 1)
        .concat([-1])
        .concat(range(this.page - 1, this.page + 2))
        .concat([-2])
        .concat(this.pagesRange.slice(-1));
    },
  },
  methods: {
    pageChange(event, newPage) {
      event.preventDefault();
      if (newPage < 1 || newPage > this.pages) {
        return;
      }
      this.$emit('change', newPage);
    },
  },
};
</script>

<style lang="scss" scoped>
.pagination-container {
  margin: 2rem 0;
  text-align: center;

  .pagination {
    margin: 0 auto;
    display: inline-flex;

    li {
      a,
      .separator {
        height: 2.5rem;
        width: 2.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.15rem;
        font-weight: 600;
        font-style: italic;
        text-decoration: none;
        background-color: transparent;
        color: #333;
      }

      .separator {
        cursor: default;
      }

      &.prev,
      &.next {
        a {
          background-color: transparent;
          color: $color-yellow;
          font-size: 28px;
          font-weight: 300;
          overflow: hidden;
          transform: rotate(90deg);
          background-size: 33%;
        }
      }

      &.next {
        a {
          transform: rotate(-90deg);
        }
      }

      &.active {
        a,
        a:hover {
          background-color: $color-yellow;
        }
      }

      a:hover {
        background-color: rgba($color-yellow, 0.15);
        text-decoration: none;
      }

      &.disabled,
      &[disabled] {
        pointer-events: none;
        filter: grayscale(1);

        a,
        a:hover {
          background-color: transparent;
          color: #333;
        }
      }
    }
  }
}
</style>
