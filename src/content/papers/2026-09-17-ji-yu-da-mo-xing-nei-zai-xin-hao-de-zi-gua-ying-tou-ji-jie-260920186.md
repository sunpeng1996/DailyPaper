---
title: 'To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model
  Signals'
title_zh: 基于大模型内在信号的自适应投机解码框架SwitchSD
authors:
- Roy Eisenstadt
- Ido Cohen
- Edo Cohen-Karlik
- Lior Wolf
- Itamar Zimerman
affiliations:
- Tel Aviv University
- Stealth Startup, Tel Aviv
arxiv_id: '2609.20186'
url: https://arxiv.org/abs/2609.20186
pdf_url: https://arxiv.org/pdf/2609.20186
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 大模型推理加速 · 投机解码优化
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Model Probing
- EAGLE3
- KV Cache
one_liner: 通过轻量探针检测大模型内在复制意图，动态切换投机解码策略，最高提效15%
practical_value: '- 电商/广告场景的Agent生成文案、商品参数描述时经常需要复制上下文结构化内容，可复用SwitchSD的复制意图探针逻辑，比纯n-gram匹配减少误复制，提升生成速度

  - 现有生成式推荐/Agent服务已用EAGLE等投机解码加速的，可直接集成SwitchSD的轻量线性探针（仅需单层线性层，开销可忽略），无需改动原有解码逻辑，就能获得最高15%的吞吐提升

  - 推理调度层面可借鉴「高复制意图场景用上下文复制、其余用神经草稿」的分治策略，针对大促等文案生成密集场景专门优化，进一步降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有投机解码（SD）分为神经草稿（如EAGLE3）和上下文复制两类，后者在复制密集场景提速明显，但纯基于n-gram匹配的启发式切换逻辑无法区分真实复制意图和意外重复（如推导中的变量名复用、文案中的固定句式巧合重叠），误触发复制会导致0接受率的「speculation tax」，反而降低整体吞吐，亟需更精准的切换决策信号。
### 方法关键点
- 提出SwitchSD自适应框架，将复制意图检测转化为二分类任务，在大模型中间层注意力子层的隐藏表示上训练无偏线性探针，AUC>0.99，仅增加可忽略的计算开销
- 构造包含强/中/无复制需求的CopyDiversity校准数据集训练探针，解决自然语料中复制样本稀疏、标签噪声高的问题
- 解码时同时满足「探针预测复制意图分数高于阈值」和「存在至少5-gram上下文匹配」两个条件才触发复制策略，否则复用原有神经草稿策略，通过lazy propagation同步KV cache，保证生成逻辑完全正确
### 关键结果
在Llama3、Qwen3系列模型上测试，覆盖代码（HumanEval）、数学推理（Math500）、摘要（CNN/DailyMail）三类场景，对比EAGLE3、CopySpec、BanditSpec等所有基线，吞吐最高比SOTA EAGLE3提升15%，代码场景加速比达2.58倍，即使在温度=1.0的高随机性生成场景仍优于所有基线。
> 最值得记住：大模型内部隐藏表示包含高价值的可解释控制信号，用轻量探针挖掘这类信号做解码调度，效率远高于黑盒启发式或统计反馈方法
