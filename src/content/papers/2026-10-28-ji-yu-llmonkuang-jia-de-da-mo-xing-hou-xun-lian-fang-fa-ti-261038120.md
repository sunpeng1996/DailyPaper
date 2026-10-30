---
title: Post-Training Large Language Models with LLMON
title_zh: 基于LLMON框架的大模型后训练方法 提升抗Prompt注入能力
authors:
- Basel Shbita
- Michael Hind
- Chad DeLuca
- Nathan Fulton
- Shubhi Asthana
- Farhan Ahmed
- Anisa Halimi
- Yada Zhu
- Mauro Martino
- David Cox
affiliations:
- IBM Research
arxiv_id: '2610.38120'
url: https://arxiv.org/abs/2610.38120
pdf_url: https://arxiv.org/pdf/2610.38120
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: LLM后训练 · 结构化指令执行绑定
tags:
- LLM Post-Training
- Prompt Injection
- LLMON
- Instruction-Data Separation
- SFT
- RLHF
one_liner: 通过LLMON结构化后训练，无架构修改下大幅降低间接Prompt注入攻击成功率并保留通用能力
practical_value: '- 可复用LLMON显式指令-数据分离+ID绑定设计，优化电商RAG/Agent系统的prompt注入防御：将用户检索到的商品评论、第三方数据全部封装为data块，仅显式引用的指令才执行，避免注入的恶意指令篡改推荐结果

  - 训练阶段的distractor augmentation trick可直接复用：在SFT数据中加入无关干扰指令/数据段，强制模型仅关注绑定的目标输入，提升推荐Agent在多上下文（用户历史、多轮对话、检索结果混杂）下的执行准确性

  - 可复用IFR/DAS/LEAK三个注意力可解释性指标，诊断业务LLM/Agent在多上下文下的注意力漂移问题：比如定位推荐系统中模型意外关注无关广告/干扰内容的层位置，针对性优化训练数据'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM对上下文所有token无差别处理，无显式指令与数据边界，导致prompt注入风险高、多指令上下文下执行歧义大，在RAG、工具调用、电商Agent等场景下极易被恶意注入的指令篡改输出，比如商品检索结果中植入的恶意指令可能诱导模型生成不符合要求的推荐内容，严重影响业务可靠性。

### 方法关键点
- 基于LLMON分层标记框架，用6个独立保留token作为分隔符，将内容分为指令、数据、执行块等带唯一ID的结构化段，仅执行块显式引用ID对应的指令和数据才会被执行
- 构建4.6B token的结构化训练语料，覆盖通用、RAG、工具调用场景，新增distractor augmentation：每个样本注入1-3条干扰指令/无关数据段，仅绑定目标段的输出被标注为正确
- 训练pipeline：先将LLMON分隔符加入tokenizer保留位，全参数SFT后接GRPO强化学习+DPO偏好优化，无需修改模型架构

### 关键结果
对比同参数Granite-4.1 Instruct baseline，在3B和8B两个尺度验证：1. 通用能力基本持平，3B模型能力无下降，8B仅下降1.4个百分点，安全指标提升6.2-8.8个百分点；2. 间接prompt注入攻击成功率从53%-100%降至0.02%-5.6%，其中文本注入（OPI）下降3个数量级，Agent工具观测注入（ASB）下降17倍以上；3. 红队测试下间接攻击鲁棒性从0.7%-2.8%提升至79.8%-84.6%。

无需修改LLM架构，仅通过结构化后训练即可让模型内化指令-数据分离的语义，大幅降低非可信输入的注入风险，是推理层防御的重要补充。
