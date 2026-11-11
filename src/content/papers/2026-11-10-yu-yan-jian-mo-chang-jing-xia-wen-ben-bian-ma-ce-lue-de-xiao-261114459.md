---
title: When does text encoding matter for language modeling?
title_zh: 语言建模场景下文本编码策略的效果差异及适用场景研究
authors:
- Eugene Jang
- Catherine Arnett
- Terra Blevins
affiliations:
- Northeastern University
- EleutherAI
arxiv_id: '2611.14459'
url: https://arxiv.org/abs/2611.14459
pdf_url: https://arxiv.org/pdf/2611.14459
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: LLM文本编码优化 · 多语言适配
tags:
- TextEncoding
- ByteLevelLM
- MultilingualLLM
- Tokenization
- UTF-8
one_liner: 对比16种文本编码策略，发现仅中、韩等高信息密度文字从压缩编码显著获益，小粒度文字对编码选择不敏感
practical_value: '- 中文/韩语的生成式推荐、Agent话术生成场景，可将默认UTF-8替换为GBK/CuTF-2等压缩编码，相同训练数据量下Macro-NLL降低6%（中文），同时token序列长度缩短30%，提升KV
  cache利用率与推理速度

  - 面向泰米尔、格鲁吉亚等小粒度文字的出海业务LLM，无需额外优化编码，默认UTF-8即可达到最优效果，减少开发与适配成本

  - 多语言混合的搜索/推荐场景可复用AETHER混合编码架构：目标语言采用专项压缩编码，其他文本回退到UTF-8，兼顾性能与全Unicode覆盖，避免OOV问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
UTF-8作为LLM默认文本编码的变长设计，导致中、韩等大字符集语言的编码长度是英文的3倍，既带来计算效率损耗，也引发跨语言公平性问题。现有研究仅针对单一编码优化，缺乏对不同编码效果的系统性对比，编码选择对模型性能的影响机制尚未明确。

### 方法关键点
- 覆盖16种编码方案：包含UTF-8/UTF-16等通用Unicode编码、GBK/Jamo等语言专属编码，以及新增的CuTF定制化固定长度编码，可灵活适配不同文字的压缩需求
- 提出AETHER混合编码框架：对目标文字应用专属编码，其余文本回退到UTF-8，解决非目标文字OOV问题，保证不同编码的对比实验公平性
- 控制变量训练：所有模型采用Llama-3 120M参数架构，固定相同训练数据量（单语言6B字符），以字符级宏观平均NLL（Macro-NLL）为核心指标，避免高频字符偏差

### 关键结果
在4种语言、38组编码对比实验中：
1. 中文/韩语（单字符信息密度高）：编码压缩率与性能强相关，最高压缩编码相比UTF-8的Macro-NLL分别降低6%、2%，相关系数r分别为0.911、0.689
2. 泰米尔/格鲁吉亚语（单字符信息密度低）：编码压缩率与性能无显著相关性，即使压缩率相差7~8倍，性能差异小于1%

### 核心结论
文本编码不是通用默认选项，而是需要根据目标文字的表意粒度定制的设计决策，仅单字符携带信息量高的语言能从压缩编码中显著获益。
