---
title: 'From Retrieval to Weights: Parametric Individualization of Small Language
  Models with Individual Text Corpora'
title_zh: 基于个体文本语料的小语言模型参数化个性化方法：从检索到权重
authors:
- Christoph Wigbels
- Ali Abusaleh
- Markus T. Jansen
- Alexander Mehler
- Markus J. Hofmann
affiliations:
- Bergische Universität Wuppertal
- Goethe-Universität Frankfurt
arxiv_id: '2609.10155'
url: https://arxiv.org/abs/2609.10155
pdf_url: https://arxiv.org/pdf/2609.10155
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 小语言模型 · 参数化个性化
tags:
- DoRA
- PEFT
- SLM
- Personalization
- RAG
- Knowledge Injection
one_liner: 通过用户专属DoRA适配器将个体文本语料注入SLM权重，验证参数化个性化的效果边界
practical_value: '- 个性化电商/教育Agent可采用「共享基座SLM+用户专属DoRA适配器」架构，每个用户仅需存储KB级适配器，成本远低于全量微调或单独维护RAG库，适配亿级用户规模的个性化场景

  - 基于用户历史行为的个性化推荐/建模任务，可利用DoRA相比LoRA更高的知识注入能力，将用户浏览/搜索/购买历史文本直接注入适配器，比仅靠RAG召回的个性化信号更稳定

  - 做用户偏好/知识的多选型评测时，可采用PMI消偏的选项内容打分法，避免模型对选项ID、文本长度的偏好bias，提升评测结果的可靠性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM存储的是群体级通用知识，无法复刻个体独有的知识结构与行为偏好；传统RAG方案做个性化需外挂用户语料库，推理成本高、长尾用户信号不稳定，参数化注入个体知识的方案效果边界尚不明确。
### 方法关键点
- 数据：采集150名用户的谷歌搜索历史构建个体文本语料（ITC），配套36道常识多选题的用户真实答题数据作为评测基准
- 训练：基座选用Qwen3-0.6B SLM并完全冻结，为每个用户训练专属DoRA适配器（r=16，全线性层适配），在用户ITC上做无标注持续预训练
- 评测：采用PMI消偏的选项内容打分法，规避模型对选项ID、文本长度的固有偏置，对比「无RAG/ITC-RAG」「基座/用户DoRA」2×2组合的效果
### 关键结果
- 文本层面：用户专属DoRA对自身未见过的ITC文本的困惑度比适配其他用户低0.107 nats/token（dz=1.27），验证适配器确实写入了用户专属信息
- 答题层面：DoRA相比基座可将用户答案的对数损失降低0.079 nats（PMI消偏下），但答题匹配准确率无显著提升，增益主要来自通用知识注入而非对用户错误偏好的对齐
- 对比RAG：ITC-RAG在DoRA基础上无额外效果增益，参数化知识注入可完全替代检索的作用

小语言模型的参数化个性化可稳定注入用户专属知识，存储与推理成本远低于RAG方案，但要复刻个体的独特行为偏好还需配套更针对性的训练目标。
