require 'test_helper'

class StaticPagesControllerTest < ActionDispatch::IntegrationTest
  test "should get aboutus" do
    get static_pages_aboutus_url
    assert_response :success
  end

end
