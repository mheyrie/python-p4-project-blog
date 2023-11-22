import React from 'react';
import {Form, Button} from 'react-bootstrap'
import{useForm} from 'react-hook-form'

function CreateBlog() {
  
  const{register, handleSubmit, reset, formState:{errors}} = useForm()


  return (
    <div className="container_blog">
      <h1>Create New Blog</h1>
      <form>
        <Form.Group>
          <Form.Label>Title: <br/></Form.Label>
          <Form.Control className="title" type="text"/>
        </Form.Group>
        <br/>
        <Form.Group>
          <Form.Label>
            Body: <br/>
            </Form.Label>
          <Form.Control className="body" as="textarea" rows={5} />
        </Form.Group>
        <Form.Group>
          <Form.Label>Min to read: </Form.Label>
          <Form.Control/>
        </Form.Group>
        <Form.Group>
          <br/>
          <Button variant="primary">
            Save
          </Button>
        </Form.Group>
      </form>
    </div>
  )
}

export default CreateBlog