---
title: What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym
title_zh: 训练代码Agent的优质数据特征：基于SWE-Gym的系统性研究
authors:
- Yikai Zhang
- Mai Xu
- Yunbei Zhang
- Qirui Jin
- Kenan Li
- Yuwen Jia
- Jinwei Yao
- Xiangyu Zhang
- Jielun Tan
- Jin Pan
affiliations:
- AMD
- University of Michigan
- Tulane University
- Georgia Institute of Technology
- University College London
arxiv_id: '2611.30207'
url: https://arxiv.org/abs/2611.30207
pdf_url: https://arxiv.org/pdf/2611.30207
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: 代码Agent训练数据质量优化
tags:
- CodingAgent
- RL
- RewardLabel
- DataCuration
- SWE-Gym
- LLM4Agent
one_liner: 审计SWE-Gym奖励标签错误，清理后的数据训练的代码Agent在公开基准最高提升2.7个点
practical_value: '- 训练业务Agent（如导购Agent、客服Agent）时，不要直接丢弃模型从未完成的任务，优先校验奖励标签的正确性，避免误删有价值的训练数据

  - 传统的训练集通过率/ reward方差过滤只能去掉几乎无梯度的标签错误，会保留19%以上带有效梯度的错误标签，这类错误需要通过执行/人工校验标签本身才能发现，可复用在推荐RL排序的
  reward 信号校验场景

  - 相同数据量和难度下，校验过标签的数据集训练效果显著优于仅做难度过滤的数据集，做Agent/RL类业务优化时，优先做标签质量审计的ROI高于单纯加数据、调模型

  - 不要用训练集上的reward指标判断数据集质量，必须用域外holdout数据集/线上指标评估，避免被有偏的训练标签误导'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RL训练代码Agent依赖任务的隐藏测试作为奖励标签，但现有数据集仅校验参考解能通过测试，无法保证所有正确解都能拿到奖励、错误解都拿不到奖励，标签错误会严重误导训练方向，目前缺少对这类错误的量化分析和影响评估。

### 方法关键点
- 对SWE-Gym的2265个可用任务逐断言审计，所有疑似错误必须通过执行复现：假阴性（正确解被拒）需要有可执行的替代解验证，假阳性（错误解通过）需要有可执行的反例验证
- 对可修复的假阴性任务通过补充issue要求修复，不可修复的移除，最终得到1087个校验后的任务组成SWE-Gym-Verified
- 控制训练集大小和难度完全一致，对比4组数据集的训练效果：原始任务集、仅做通过率过滤的原始任务集、校验后任务集、补充反例测试的校验后任务集

### 关键实验
用9B参数Qwen3.5模型做GRPO训练，与基线原始任务集相比：校验后的Clean集在SWE-bench Verified上pass@1高2.4个点，在SWE-bench Pro上高2.7个点；仅做通过率过滤的集合没有显著提升；补充反例测试过滤25%假阳性后，域外指标无可检测的变化。另外发现74%的模型从未解决的任务存在假阴性错误，而非本身难度过高。

### 最值得记住的一句话
Pass rate only tells whether a task yields reward, not whether that reward is right
