---
title: 'A Conditional No-Hair Theorem for Transformers: How Language Models Forget
  Their Prompt'
title_zh: Transformer条件无毛定理：大语言模型对Prompt的遗忘机制
authors:
- Shuyang Xiang
affiliations:
- Independent Researcher
arxiv_id: '2610.24133'
url: https://arxiv.org/abs/2610.24133
pdf_url: https://arxiv.org/pdf/2610.24133
published: '2026-10-15'
collected: '2026-10-20'
category: LLM
direction: 大语言模型 · Prompt记忆衰减机制
tags:
- Transformer
- Prompt Engineering
- Long Context
- Theoretical Bound
- Attention Mechanism
one_liner: 量化Transformer生成过程中prompt影响的幂律衰减规律并给出理论边界
practical_value: '- 多轮对话Agent（如电商客服、导购）设计中，若需长期遵守系统指令，可每8-15轮隐式/显式重复核心规则，阈值可参考本文测得的α指数校准

  - 长上下文生成式推荐场景中，用户初始偏好prompt的影响会随生成内容长度快速衰减，高优先级偏好需嵌入到最近几轮交互中而非仅放在对话开头

  - 可通过给prompt token添加固定logit偏置缓解遗忘，实测温和偏置可提升10%-15%的指令遵循率，仅带来小于2%的perplexity上升，适合对规则敏感性高的广告文案生成、合规客服场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大语言模型在长对话、长生成任务中普遍存在prompt遗忘问题，例如系统指令漂移、Agent约束失效，但此前缺乏量化的衰减规律和理论解释，无法指导工程上优化长上下文下的prompt有效性。

### 方法关键点
- 设计teacher-forcing对照实验：固定两个不同prompt后的续接文本完全一致，仅通过隐层状态差值度量prompt的残留影响，排除生成文本差异的干扰
- 定义衰减指数α：prompt残留信号随生成token数t的衰减符合$t^{-α}$幂律，β度量隐层噪声的衰减，实测β≈0，仅用α即可衡量遗忘速度
- 提出条件无毛定理：在pre-LN、因果注意力、logit有界的架构下，prompt影响的衰减上界为$O(P(\log t)^{L-1}/t)$，P为prompt长度，L为模型层数
- 分解注意力路径为直接路径（query直接关注prompt）和relay路径（query关注携带prompt信息的续接token），解释训练对衰减速度的影响

### 关键结果
- 未训练模型遗忘较慢，α≈0.2-0.5，且层数越深α越小（记忆保留越久）
- 训练后模型遗忘速度显著加快，浅层α≈0.9-1，深层稳定在0.55-0.7，与模型大小、架构（Pythia/Qwen）无显著差异

**最值得记住的结论**：只要生成内容足够长，prompt的影响最终会完全消失，留存的信息一定已经被编码到已生成的文本中
