---
title: 'Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe
  Inputs'
title_zh: 文本感知但视觉盲：多模态图像编辑系统的不安全输入处理研究
authors:
- Ziqing Yang
- Yixin Wu
- Michael Backes
- Yang Zhang
affiliations:
- CISPA Helmholtz Center for Information Security
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2611.26569'
url: https://arxiv.org/abs/2611.26569
pdf_url: https://arxiv.org/pdf/2611.26569
published: '2026-11-19'
collected: '2026-11-21'
category: Eval
direction: 多模态图像编辑系统安全评估
tags:
- Multimodal Safety
- Benchmark
- Image Editing
- Content Moderation
- Safety Guardrail
one_liner: 构建含5940组样本的图像编辑安全基准EditSafetyBench，揭示多模态系统跨模态安全防护缺失问题
practical_value: '- 做图文多模态生成类业务（如商品图AI编辑、营销素材AI生成）时，安全审核必须同时校验输入文本prompt + 输入图像两个模态，不可仅校验文本

  - 涉性内容的视觉识别可直接复用成熟NSFW检测能力，政治、暴力等风险类型需额外补全跨模态联合校验规则

  - 自研多模态系统安全围栏时，可复用EditSafetyBench的11类风险+3类编辑意图划分逻辑搭建自测用例集'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多模态图像编辑系统的安全机制仅依赖单模态校验，未同时覆盖文本指令与上传图像的双重风险，存在系统性安全漏洞。

### 方法关键点
发布EditSafetyBench评测基准，包含5940组图像-指令配对样本，覆盖11类风险场景、3种编辑意图，针对Gemini、GPT、Qwen API、Qwen Local 4个主流系统做系统级安全表现评测。

### 关键结果数字
1. Gemini、GPT对含风险指令的请求拒答率分别达87.1%、81.6%，但对「风险图像+中性指令」的请求拒答率仅24.2%、22.4%；
2. 不同系统风险判定一致性差，GPT允许70.4%的涉政风险内容编辑请求，Gemini仅允许34.8%；
3. 仅涉性内容视觉检测敏感度最高，得益于成熟NSFW检测技术积累。
