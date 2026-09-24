---
title: 'When Context Misleads: In-context Learning with Jurisdiction in Large Language
  Models'
title_zh: 上下文误导场景下具备管辖权判断的大模型上下文学习方法
authors:
- Pei-lin Li
- Qingle Liu
- Junyang Feng
- Siyu Li
- Sunqi Fan
- Xin-Sheng Chen
- Shuojin Yang
affiliations:
- Tsinghua University
- Huazhong University of Science and Technology
arxiv_id: '2609.27603'
url: https://arxiv.org/abs/2609.27603
pdf_url: https://arxiv.org/pdf/2609.27603
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 大模型上下文学习鲁棒性优化
tags:
- In-Context Learning
- Post-training
- Robustness
- Benchmark
- Misleading Context
one_liner: 提出J-ICL后训练框架与伪造上下文评测集，同步提升ICL性能与抗误导上下文能力
practical_value: '- 电商导购Agent、客服LLM可复用J-ICL正负样本配对训练思路，混合「用户提供规则适用/不适用」的SFT样本，无需额外标签即可提升抗用户错误前提误导的能力，避免优惠计算、规则解答错误

  - 生成式推荐、RAG系统可借鉴J-ICL隐式管辖权判断训练方式，无需新增分类头，用常规LM loss即可训练模型自动判断检索/用户提供的上下文是否适配当前查询，过滤过期、无效规则

  - 业务LLM评测可参考FAKECONTEXT-BENCH设计思路，构造「上下文自洽但不符合业务规则」的测试用例，评估模型抗误导能力，提前发现上线后可能出现的逻辑错误'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有ICL优化方法默认所有上下文演示具备权威性，仅强化规则提取能力，导致模型易被自洽但错误的误导上下文诱导输出错误结果；大模型scaling不仅无法自发解决该问题，反而会降低抗误导能力，常规ICL后训练甚至会使事实准确率最多下降14.95pp，缺乏对应评测基准与解决方案。
### 方法关键点
- 发布**FAKECONTEXT-BENCH**评测集：覆盖7个领域共3500个样本，每个样本包含自洽错误规则+匹配演示，同时标注事实答案与上下文诱导答案，精准衡量模型上下文管辖权判断能力
- 提出**J-ICL**后训练框架：构造两类episode，J+（上下文规则适用需遵循）、J-（上下文规则不适用需返回权威答案），无需显式管辖权标签，仅对查询答案部分用常规因果LM loss优化
- 训练策略：混合三类损失（通用J+样本损失、J+/J-配对对比损失、J-/J-跨误导规则配对损失），用动态权重课程学习平衡任务，提升模型泛化性
### 关键结果
在Qwen3、Llama3.1共4个不同尺寸backbone上测试，对比Base、MetaICL、Symbol Tuning baseline：J-ICL平均提升ICLEval 5.84pp，事实准确率提升9.20pp，相比现有ICL方法Reality Rate平均提升18.09pp，且不损失常规ICL性能。
> 最值得记住的结论：可靠的ICL需要选择性而非无条件地遵循上下文演示。
