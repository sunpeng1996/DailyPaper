---
title: ReOrder-OPD:Reliability-Aware Prompt Ordering for On-Policy Distillation
title_zh: ReOrder-OPD：面向在线策略蒸馏的可靠性感知Prompt排序方法
authors:
- Ximo Zhu
- Ruiqi Liu
- Rong Wang
- Ping Wu
- Xiang Zheng
- Wenzhuo Xu
- Xubin Yao
- Zhiyuan Yan
- Bo Li
- Jun Gao
affiliations:
- Hello Group Inc.
- 中国科学院自动化研究所
- 中国科学院大学
- 北京大学
arxiv_id: '2608.10905'
url: https://arxiv.org/abs/2608.10905
pdf_url: https://arxiv.org/pdf/2608.10905
published: '2026-08-11'
collected: '2026-08-12'
category: Training
direction: 大语言模型 · 在线策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Curriculum Learning
- LLM Training
- Prompt Scheduling
one_liner: 提出基于教师续答可靠性的Prompt排序策略，不修改蒸馏损失即可显著提升在线策略蒸馏效果
practical_value: '- 做垂域小模型OPD蒸馏时（如电商Agent、生成式推荐专用小模型），可直接加入ReOrder-OPD的Prompt调度层，无需修改原有蒸馏损失，即可获得稳定效果提升，改造成本极低

  - 复用ROUGE-5最大值的可靠性Proxy设计，无需多次调用大模型教师做前缀续答，仅需提前构建同prompt下的正确教师回答库，工程实现简单、计算开销小

  - 现有轨迹级OPD优化（如FiRe-OPD、ExOPD）可直接和该Prompt调度方法叠加，两者互不冲突，可获得叠加收益，适合已经在使用轨迹级蒸馏优化的业务场景

  - 动态刷新未训练Prompt优先级的思路可迁移至Agent持续训练场景，随模型迭代重新评估未训练样本的优先级，适配模型能力变化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
On-Policy Distillation（OPD）通过在学生生成的轨迹上施加教师监督解决离线蒸馏的训练/测试分布偏移问题，但教师从学生生成前缀续出的结果可能不正确，导致监督信号不可靠。现有方法仅在单条采样轨迹内部做加权、截断、过滤，容易把单次轨迹的不可靠归因为prompt本身训练价值低，且已有研究证实prompt训练顺序对OPD效果影响显著，但缺乏针对性的调度方案。

### 方法关键点
1. 定义prompt级教师续答可靠性R：教师从当前学生生成的任意前缀续出正确答案的平均概率，Oracle实验验证高R prompt的训练增益显著高于低R样本，按R降序训练效果远超随机、升序以及按难度/学生正确率排序的方案。
2. 设计低成本R proxy：无需多次采样教师前缀续答，仅用1条学生独立生成的回复与同prompt下已验证正确的所有教师回复的最大ROUGE-5 F1作为排序分数，该proxy的10个等频分位的平均R从0.29单调上升至0.98，可有效区分粗粒度可靠性层级。
3. 实现ReOrder-OPD：静态版本用初始学生计算proxy并降序排列prompt，训练时每个prompt都重新采样学生轨迹，不复用打分轨迹；动态版本训练中定期对未访问的prompt重新打分排序，适配学生能力变化，可直接叠加任意现有轨迹级OPD优化方法。

### 关键结果
- 数学推理任务：覆盖Qwen3、Gemma4两个系列共5个不同规模学生模型，六组基准平均准确率较基准OPD提升1.09~2.58个百分点；
- 代码生成任务：Qwen3-1.7B、4B学生的多基准平均准确率较基准分别提升0.82、1.34个百分点；
- 兼容验证：叠加FiRe-OPD、ExOPD两类轨迹级优化时，3个学生规模共6组组合全部获得增益，最高提升3.33个百分点；
- 动态排序：在17K规模数据集上，动态刷新排序较静态版本进一步提升0.73~1.15个百分点。

> 最值得记住的一句话：OPD的prompt训练价值不取决于自身难度或学生单次正确率，而取决于教师能否在学生当前状态下从其生成前缀续出正确结果，仅调整prompt顺序即可在零额外训练成本下稳定提效。
