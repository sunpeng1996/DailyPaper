---
title: 'DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning'
title_zh: DoubtLess：无需训练的对比解码方法实现高效推理
authors:
- Minghao Luo
- Liang Chen
affiliations:
- The Chinese University of Hong Kong
- EPFL
arxiv_id: '2610.18862'
url: https://arxiv.org/abs/2610.18862
pdf_url: https://arxiv.org/pdf/2610.18862
published: '2026-10-12'
collected: '2026-10-14'
category: Reasoning
direction: 大模型推理 · 无训练对比解码
tags:
- Contrastive Decoding
- Chain-of-Thought
- Training-Free
- Efficient Reasoning
- LLM Inference
one_liner: 用同系列小模型的简洁/冗长思考logit差引导大模型，无训练缩短31%思考token且精度不变
practical_value: '- 电商搜推/客服Agent推理优化可复用同系列小模型双prompt对比logit修正思路，无需微调大模型即可压缩思考链长度，降低推理成本

  - 动态逐step计算logit差的方案无需硬ban关键词或用固定引导向量，不会损伤关键推理步骤准确性，适合对效果敏感的广告文案生成、商品决策Agent场景

  - 该方法可与已做长度惩罚微调的定制大模型叠加，额外压缩29%-52%思考token，适合已有业务定制模型进一步降本

  - 工程上可复用vLLM的paged KV cache同时存储大模型和两个小模型分支的缓存，小模型推理可与大模型并行，端到端latency可降低24%，落地成本低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前CoT推理模型存在严重的过度思考问题，32%-69%的思考token生成于正确答案首次出现之后，多为冗余重复校验内容，既推高推理成本又增加响应延迟；现有CoT压缩方案要么需要针对每个模型做额外微调，要么依赖固定关键词拦截、静态引导向量或提前截断规则，容易损失推理精度。

### 方法关键点
- 完全训练-free，仅采用与大模型同tokenizer的小尺寸推理模型作为引导源，小模型分别输入「要求简洁直接输出答案」和「要求详尽反复校验」两个prompt，得到两组对应logit
- 大模型每步解码时，将原生logit加上缩放因子α乘以（简洁logit - 冗长logit）的差值，仅在<think>与</think>的思考阶段生效，答案生成阶段完全不干预
- 仅调整大模型原生top-p候选范围内的token权重，不会引入大模型不会生成的内容，且保留</think>和EOS的大模型原生logit，避免不合理强制截断

### 关键结果
在7个推理基准（竞赛数学、研究生科学题、编程题）测试，用Qwen3-0.6B引导Qwen3-32B，效果优于5个推理时baseline，**缩短31%思考token且精度无损失**；在自调试编码Agent上减少20%每轮思考token，任务表现不变；适配EXAONE、Granite两个模型族，压缩量是简洁prompt的3倍；和训练好的精简模型叠加还能再压缩29%-52%token，端到端latency降低24%。

最值得记住的一句话：用同系列小模型双prompt的动态对比信号做推理优化，零训练成本即可实现精度无损的推理降本，鲁棒性远优于静态规则和单一prompt引导。
