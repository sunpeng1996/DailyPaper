---
title: 'StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for
  Calibrated Deliberative Decisions'
title_zh: StartLux-Decision：结合强化学习的校准式自适应决策模型系列
authors:
- Xialie Zhuang
- Zunhai Su
- Jia Pan
- Ngai Wong
- Guanhua Chen
- Chuan-Wei Kuo
affiliations:
- StartLux
- The University of Hong Kong
- Southern University of Science and Technology
arxiv_id: '2610.17309'
url: https://arxiv.org/abs/2610.17309
pdf_url: https://arxiv.org/pdf/2610.17309
published: '2026-10-11'
collected: '2026-10-15'
category: LLM
direction: LLM决策模型 · 自适应推理优化
tags:
- Decision Model
- Reinforcement Learning
- Adaptive Reasoning
- Probability Calibration
- Efficient Inference
one_liner: 推出0.8B-27B双版本决策模型系列，通过置信度引导自适应推理+RLCD2平衡效果与效率
practical_value: '- 推荐系统路由场景可复用置信度门控逻辑：高置信度简单请求用轻量单pass模型返回，低置信度复杂请求才调用重推理模块，平衡时延与业务效果

  - 生成式推荐/Agent工具调用的RL优化可复用RLCD2奖励设计：除正确性奖励外，增加推理长度软惩罚+概率校准奖励，平衡推理效率与输出可靠性

  - 单pass分类/判分任务可引入prompt双向注意力改造：无需新增预测头，仅修改全注意力层为双向注意力即可提升效果，适配内容审核、标签判定等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有开源决策模型多采用单pass预测，效率高但在规则校验、算术推理、工具调用判断等需多步计算的复杂决策上表现较差；引入推理的方案普遍存在推理长度不可控、终止率低、概率校准偏差大的问题，难以适配推荐、电商、Agent等对时延和可靠性要求极高的落地场景。
### 方法关键点
- 双版本模型设计：Instant版采用全注意力层双向注意力，单pass输出决策概率，推理效率极高；AutoThink版采用置信度门控Read-or-Think机制，置信度≥0.9直接返回结果，低于阈值才触发推理，融合推理前后概率输出最终结果。
- 三阶段训练Pipeline：阶段1全参数SFT训练基础决策能力；阶段2用Adapter分别适配双向注意力（Instant）和因果注意力（AutoThink）；阶段3先做推理监督，再用RLCD2强化学习优化推理策略，奖励为推理前后概率质量差值，加推理长度超预算的软惩罚。
- 提出policy-aware校准方法，结合下游路由/选路逻辑修正置信度，解决单样本校准与实际部署后置信度偏差的问题。
### 关键实验结果
在Decision Index 0.3公开子集上，Instant版比同规模SOTA开源决策模型高7.4~16.9分；在针对细节敏感度的DecisionPivot基准上，AutoThink版比Instant版高11.5~18.4个百分点，27B版本达到86.9%的配对准确率；RLCD2将推理终止率最高提升48个百分点，平均推理长度降低65%，几乎不损失决策精度。
> 最值得记住的一句话：决策系统的优化核心是在效果、效率、可靠性三者之间找动态平衡，而非一味追求单指标最优。
