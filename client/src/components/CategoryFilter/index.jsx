import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'

import * as Styles from './styles'
import Button from '../Button'
import {setFilteredProductsAction} from '../../store'


const CategoryFilter = (props) => {
  const categories = props.categories

  const dispatch = useDispatch()
  const products = useSelector(state => state.products)

  const [selectedCategory, setSelectedCategory] = useState('All')

  const filterByCategory = (category) => {
    let filteredProducts = products.filter((product) => product.categoryName === category)
    if (filteredProducts.length === 0) {
      dispatch(setFilteredProductsAction(products))
    } else {
      dispatch(setFilteredProductsAction(filteredProducts))
    }
    setSelectedCategory(category)
  }

  return (
    <Styles.FilterOptions>
      <Button active={selectedCategory === 'All'} onClick={() => filterByCategory('All')}>Усі</Button>
      {categories.map((category, index) => (
        <Button
          key={index}
          active={selectedCategory === category.categoryName}
          onClick={() => filterByCategory(category.categoryName)}>
          {category.categoryNameUkr}
        </Button>
      ))}
    </Styles.FilterOptions>
  )
}

export default CategoryFilter