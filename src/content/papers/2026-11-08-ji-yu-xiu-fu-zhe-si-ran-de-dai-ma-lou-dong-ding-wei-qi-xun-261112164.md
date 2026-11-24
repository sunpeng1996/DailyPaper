---
title: 'Let the Fixer Decide: Training a Code Localizer from the Fixer''s Likelihood'
title_zh: 基于修复者似然的代码漏洞定位器训练方法
authors:
- Khalil Hennara
- Muhammad Hreden
- Zeina Aldallal
- Sara Chrouf
- Safwan AlModhayan
affiliations:
- Misraj AI, Saudi Arabia
arxiv_id: '2611.12164'
url: https://arxiv.org/abs/2611.12164
pdf_url: https://arxiv.org/pdf/2611.12164
published: '2026-11-08'
collected: '2026-11-24'
category: Agent
direction: 代码Agent · 定位模块训练优化
tags:
- Agent
- LoRA
- Supervised Fine-Tuning
- EM Algorithm
- Code Localization
one_liner: 无需强化学习与测试运行，通过加权监督微调训练高效代码漏洞定位器
practical_value: '- 可复用「下游模块打分、上游子模块加权SFT优化」的范式，替换推荐/搜索召回模块的人工标注正负样本训练，用下游排序/转化率信号加权微调，更贴合业务最终效果，无需RL即可降低对齐成本

  - 跨折模型打分的防泄露技巧可直接复用，训练检索/召回模块时，必须用未见过当前样本的下游模型生成权重信号，避免模型记忆导致训练信号失效

  - 小参数模型落地优先排查瓶颈：推理速度、上下文溢出、重复生成问题的优先级远高于子模块精度，否则上游优化的收益会被下游瓶颈完全消耗

  - 线上AB测或离线评估要做多次配对测试，小样本下相同模型的结果波动可达30%以上，不能仅靠单次准确率判定效果优劣'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统代码定位器以参考补丁修改的文件作为监督标签，但修复者实际需要读取的代码不止修改部分，现有标签信号弱；而此前从修复结果学习的方法依赖强化学习+测试运行，算力与时间成本极高，亟需低成本的定位器优化方案。

### 方法关键点
1. 双LoRA架构：同一Gemma 4 E4B基础模型挂载两个独立LoRA，分别作为固定的修复者和待训练的定位器，修复者调用定位器获取最多8个代码位置后执行修复流程
2. Fixer-Guided Localization（FGL）范式：定位器生成多个候选定位结果，固定修复者计算每个候选下生成验证通过补丁的对数似然，叠加代码长度、额外读取请求的惩罚后得到分数，经软最大化后作为权重对定位器做加权监督微调
3. 跨折训练防泄露：训练数据拆为两折，仅用未见过当前任务的折外模型生成候选、计算分数，避免模型记忆导致训练信号失效
4. 增加教师定位结果的锚定损失，权重设为0.5，避免定位器训练漂移

### 关键结果数字
离线测试在1016个训练任务上，最优候选定位比教师定位的代码量少27.5%，上下文溢出减少44%，修复者首次命中补丁位置的准确率相当（43.1% vs 42.4%）；线上78个开发任务测试中，EM训练后的Agent生成有效补丁的任务数更多（53 vs 46），无效文件读取错误更少（43 vs 54），解决任务数略高于基线（8 vs 6）但未达统计显著。

**最值得记住的一句话：小参数Agent的性能瓶颈通常是推理速度、重复循环、输出质量，而非上游子模块的精度，优化要优先解决瓶颈问题。**
