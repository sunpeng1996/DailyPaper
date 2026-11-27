---
title: 'Know the Design, Pick the Attack: Sentence-Keyed Watermarks for LLMs'
title_zh: 基于句子密钥的大语言模型抗自适应攻击文本水印方案
authors:
- Jon Carmona
- Jon Irureta
- Jon Imaz
- Aizea Lojo
- Juan Martínez-Romo
- Lourdes Araujo
arxiv_id: '2611.34505'
url: https://arxiv.org/abs/2611.34505
pdf_url: https://arxiv.org/pdf/2611.34505
published: '2026-11-25'
collected: '2026-11-27'
category: LLM
direction: 大语言模型 · 文本水印攻防
tags:
- LLM-Watermark
- Text-Provenance
- Adversarial-Attack
- Dynamic-Key
- Content-Tracing
one_liner: 基于前文语法提取动态密钥的KeyedLex水印，显著提升LLM文本水印抗自适应攻击能力
practical_value: '- 生成式推荐/Agent输出的营销文案、商品介绍等内容可复用KeyedLex水印方案，溯源生成内容同时抗paraphrase篡改，避免恶意盗用生成内容用于违规营销

  - 针对LLM生成内容的溯源需求，水印嵌入无额外计算开销，不影响生成文本的可读性与流畅度，可直接接入业务侧LLM输出链路

  - 应对公开水印方案被针对性破解的问题，可参考「密钥从生成文本上下文动态提取」的设计思路，无需存储静态密钥，降低被批量伪造的风险'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM水印方案公开设计后易被攻击者针对性选择破解方式：对难学习的水印采用重写擦除，对耐重写的水印直接学习伪造，所有现有方案在该自适应攻击下均失效，亟需抗攻击能力更强的水印方案支撑生成内容溯源、虚假信息治理、合规性校验等需求。
### 方法关键点
KeyedLex水印方案的密钥从前一句的语法特征中动态提取，重写改写对语法特征改动极小，且检测器无需精确还原密钥即可识别水印，不依赖静态密钥存储，嵌入逻辑无额外计算开销。
### 关键结果数字
在两个测试模型上性能均优于对比的所有现有水印方案，攻击后仅损失约50%的水印信号，而最优对比方案损失达2/3，且生成文本质量与业界最优水印方案相比无额外下降。
