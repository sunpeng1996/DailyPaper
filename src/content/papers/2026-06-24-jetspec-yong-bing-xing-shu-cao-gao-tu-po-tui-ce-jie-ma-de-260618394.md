---
title: 'JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel
  Tree Drafting'
title_zh: JetSpec：用并行树草稿突破推测解码的扩展上限
authors:
- Lanxiang Hu
- Zhaoxiang Feng
- Yulun Wu
- Haoran Yuan
- Yujie Zhao
- Yu-Yang Qian
- Bojun Wang
- Peng Zhao
- Daxin Jiang
- Yibo Zhu
affiliations:
- UC San Diego
- Zhejiang University
- UIUC
- Nanjing University
- StepFun
arxiv_id: '2606.18394'
url: https://arxiv.org/abs/2606.18394
pdf_url: https://arxiv.org/pdf/2606.18394
published: '2026-06-24'
collected: '2026-06-27'
category: LLM
direction: LLM推理优化 · 推测解码加速
tags:
- Speculative Decoding
- LLM Inference
- Tree Drafting
- Causal Masking
- Parallel Decoding
one_liner: 提出带分支因果约束的并行树草稿框架JetSpec，突破推测解码加速扩展上限
practical_value: '- 架构选型：业务侧若用LLM做长文本生成（如商品种草文案、Agent多步推理、搜索query扩写），可复用「冻结目标模型+轻量因果并行草稿头+树验证」的speculative
  decoding架构，在无损生成质量的前提下降低延迟，无需额外部署独立草稿模型

  - 训练trick：适配业务场景训练草稿头时，优先用「目标模型再生的业务域序列 + forward KL蒸馏损失」，相比直接用原始语料、reverse KL或SFT，能显著提升草稿接受率，该结论可直接复用

  - 工程调度：线上LLM服务可根据实时负载动态调整树草稿的token预算：低负载（如单用户Agent会话、长尾query生成）用128~256大预算拿高加速比，高负载（如大促批量文案生成、热门搜索suggestion）用16~32小预算保吞吐，平衡延迟与吞吐

  - 树构建策略：做多候选生成类任务（如多query推荐、多版本文案A/B测试）时，树扩展可采用「累积对数概率打分的best-first策略」，相比熵引导或混合策略，候选质量与后续转化效果更优'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
自回归LLM的串行解码机制让延迟成为长生成场景（数学推理、编码、Agent任务等）的核心瓶颈。推测解码（SD）通过先生成草稿token再并行验证实现加速，但存在扩展天花板：增加草稿预算仅在接受率高、草稿开销低时能转化为加速收益。现有头式SD方法陷入因果-效率困境：自回归草稿器（如EAGLE）的路径条件候选接受率高，但草稿开销随树深度线性增长；双向块扩散草稿器（如DFlash）一次生成多token开销低，但分支无关的边际分布会生成语义矛盾的树分支，浪费预算、拉低接受率，无法通过扩大预算持续提效。

**方法关键点**
- 架构：采用头式设计，轻量草稿头复用冻结目标模型的多层融合隐藏特征，无需独立部署草稿模型，大幅降低草稿开销与部署成本
- 核心创新：给草稿头施加**树因果注意力掩码**——每个树节点仅可见前缀与自身祖先分支，不可见后代或兄弟节点，既支持所有树节点单次前向并行生成，又保证每个分支的分布是路径条件的，与目标模型的自回归因式分解完全对齐，从结构上避免分支矛盾
- 训练：用目标模型再生的序列做训练数据，采用forward KL蒸馏损失对齐草稿分布与目标模型的软标签偏好，保留多候选的相对概率，更适配树扩展场景
- 树构建与验证：用累积草稿对数概率做分支打分，best-first优先扩展高分分支填充预算；目标模型用树注意力并行验证所有节点，接受最长一致前缀，保证生成质量无损

**关键实验**
- 测试模型：Qwen3-8B（稠密）、Qwen3-30B-A3B（MoE），基线为EAGLE-3、DFlash、DDTree，所有方法用相同训练数据与算力
- 覆盖数据集：数学（GSM8K、MATH-500、AIME25）、编码（HumanEval、MBPP、LiveCodeBench）、开放对话（MT-Bench）
- 核心结果：H100 GPU上，256 token草稿预算下，JetSpec在MATH-500（greedy）达9.64×端到端加速，MT-Bench达4.58×；MoE模型上MATH-500仍达9.45×；集成vLLM后，低负载下单卡H100服务加速超6×，高负载下小预算（16-32）更适配吞吐需求

**核心洞见**
推测解码的加速上限由草稿开销和接受率共同决定，给并行草稿头增加分支级因果约束，是在低草稿开销下维持高接受率、突破扩展天花板的关键
