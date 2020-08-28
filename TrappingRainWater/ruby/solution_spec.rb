require 'rspec'
require_relative 'solution.rb'

describe "Solution Tests" do
    it "empty" do
        expect(trap([])).to eq 0
    end

    it "hill" do
        expect(trap([0, 1, 2, 1, 0])).to eq 0
    end

    it "bowl" do
        expect(trap([2, 1, 0, 1, 2])).to eq 4
    end

    it "normal" do
        expect(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])).to eq 6
    end
end
