.PHONY: fetch-main merge-main push-main publish serve

# Process blog posts before serving
process-posts:
	@echo "Processing blog posts..."
	bundle exec ruby _scripts/process_posts.rb

# Serve Jekyll site locally for testing
serve: process-posts
	@echo "Starting Jekyll server..."
	bundle exec jekyll serve

