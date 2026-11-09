---
title: Beyond Truncation? Entailment-Licensed Elision and the Limits of Semantic Preservation
  in LLM Decoding
title_zh: 超越截断？LLM解码的蕴涵许可省略与语义保留边界研究
authors:
- Mahmoud Alyosify
- Mirna Imbabi
- Eman Elkhamisi
affiliations:
- School of Computing, Queen's University, Canada
arxiv_id: '2611.08975'
url: https://arxiv.org/abs/2611.08975
pdf_url: https://arxiv.org/pdf/2611.08975
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM解码优化 · 无训练冗余控制
tags:
- LLM Decoding
- Entailment
- Text Compression
- Training-free
- Semantic Preservation
one_liner: 揭示无训练LLM冗余缩减方法多为截断伪装，提出语篇限定的蕴涵许可省略方案，有害省略率降至约10%
practical_value: '- 电商Agent/LLM导购做回复精简时，必须把等长截断作为必测baseline，避免把截断伪装成智能冗余压缩，做无效投入

  - 可直接复用ELIDE的轻量省略架构：不修改LLM生成逻辑、不改动KV cache仅在输出层做span过滤，工程改造成本极低，适合客服回复、商品长文案精简场景

  - 自动指标（BERTScore、NLI相似度）无法完全检测省略的语义损伤，落地时必须加小样本人工抽检，尤其是涉及商品属性、优惠信息的场景，避免关键信息被误删

  - 无训练冗余压缩的实际增益有限，常规LLM回复中可安全省略的冗余占比仅1-3%，性价比远低于prompt引导生成简洁内容'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
指令微调LLM普遍存在回答冗余问题，生成token数与推理成本、用户阅读负担线性正相关，现有无训练冗余缩减方法普遍仅用自动指标评估，未与最朴素的等长截断做对比，大量方法本质是伪装的截断，实际语义保留效果未达宣称水平。
### 方法关键点
- 提出「截断前沿」作为冗余缩减方法的统一评估基准：仅当方法在等长条件下的语义保留效果优于原回答前缀截断，才算真正实现冗余压缩
- 设计熵门控logits处理器（EGP），可实现19.9%~34.9%的token缩减，但严格证明其输出本质是原回答的前缀，等价于截断
- 提出ELIDE框架：生成过程中在句子边界做span判断，仅当当前span内容被已展示文本蕴涵时才对用户隐藏，隐藏span仍保留在KV cache中不改变生成轨迹；v2版本增加语篇范围限定，仅允许同列表项、同段落内的蕴涵内容被省略，避免跨单元误判
### 关键结果
在MT-Bench、AlpacaEval等共1625个prompt测试：ELIDE v1版本59%的省略会损伤语义，所有自动指标均无法检测；v2版本将有害省略率降至约10%，仅省略0.9%~2.9%的展示token，始终优于等长截断，额外推理开销仅1%~3%。
### 核心结论
所有解码阶段的文本压缩方法都必须先和等长截断做对比，自动指标无法替代人工抽检评估语义损伤。
