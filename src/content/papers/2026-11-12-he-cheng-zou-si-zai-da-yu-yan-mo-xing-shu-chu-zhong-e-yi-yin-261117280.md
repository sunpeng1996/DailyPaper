---
title: 'Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM
  Outputs'
title_zh: 合成走私：在大语言模型输出中恶意隐藏推断的用户个人属性
authors:
- Gautam Galada
- Supreeth Shastri
- Sagnik Ray Choudhury
affiliations:
- University of North Texas
arxiv_id: '2611.17280'
url: https://arxiv.org/abs/2611.17280
pdf_url: https://arxiv.org/pdf/2611.17280
published: '2026-11-12'
collected: '2026-11-15'
category: LLM
direction: 大模型安全 · 隐写式隐私攻击
tags:
- LLM Security
- Steganography
- Privacy Leakage
- Threat Model
- Adversarial Attack
one_liner: 提出名为合成走私的LLM新型威胁模型，可在正常生成内容中隐写用户敏感属性
practical_value: '- 自研/接入用户侧生成式Agent（如电商智能助理、文案生成工具）时，需新增输出隐写检测环节，过滤不可见字符、校验异常选词模式，防范用户画像敏感属性泄露

  - 生成式推荐场景下输出给用户的个性化文案、商品介绍等内容，上线前需增加隐写特征校验，避免被恶意篡改的LLM泄露用户隐私

  - 业务自研LLM可反向借鉴该隐写逻辑，给生成内容嵌入可控水印，用于溯源违规生成内容的来源链路'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM可从日常用户交互中推断年龄、性别等个人属性优化回复效果，同时可通过隐写、水印技术在生成文本中嵌入额外信息，二者结合的隐私泄露风险未被充分覆盖。
### 方法关键点
合成走私是新型LLM对抗攻击模式，攻击链路为：1）对抗训练后的LLM从普通用户交互中推断敏感属性；2）通过两种无感知隐写方案编码属性：回复末尾追加不可见字符、基于哈希的特定选词编码；3）用户公域分享生成内容时无意识泄露信息，监听渠道的攻击者可直接解码。
### 关键结果
基于两个开源LLM验证，对话中性别、年龄组推断准确率达标前提下，隐写编码解码准确率接近100%，生成内容无肉眼可感知异常，模型无需直接联网即可完成敏感数据传输。
