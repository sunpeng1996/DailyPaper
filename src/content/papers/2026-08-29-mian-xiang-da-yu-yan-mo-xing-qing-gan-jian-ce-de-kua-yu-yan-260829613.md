---
title: Cross-lingual Functional Vectors for Emotion Detection in Large Language Models
title_zh: 面向大语言模型情感检测的跨语言功能向量
authors:
- Jieying Xue
- Phuong Minh Nguyen
- Minh Le Nguyen
- Shogo Okada
affiliations:
- Japan Advanced Institute of Science and Technology
arxiv_id: '2608.29613'
url: https://arxiv.org/abs/2608.29613
pdf_url: https://arxiv.org/pdf/2608.29613
published: '2026-08-29'
collected: '2026-09-01'
category: LLM
direction: 大语言模型 · 激活干预跨语言迁移
tags:
- Function Vector
- Cross-lingual Transfer
- Emotion Detection
- Activation Steering
- In-context Learning
one_liner: 验证功能向量具备跨语言迁移性，无需微调即可大幅提升多语种情感分类性能
practical_value: '- 多语种业务场景（如跨境电商评论情感分析、多语种广告话术情绪判别）可直接复用跨语言FV方案，仅用单语言标注数据即可实现多语种任务迁移，大幅降低小语种标注成本

  - 线上推理时注入FV替代部分few-shot样例，可减少KV cache占用、降低推理时延，适合高吞吐的实时情感判别场景（如直播实时评论风控、多语种客服情绪识别）

  - FV构建时优先选择跨层分布的top-20以内高贡献注意力头，单模型的最优头选择范围稳定跨语言通用，无需针对每个语言单独调优

  - 小语种任务可先用英文标注提取FV再注入目标语言推理，效果接近同语言FV，适合缺少小语种标注数据的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Function Vector（FV）研究多聚焦于简单单语种结构化任务，在情感分析这类需上下文语义理解的复杂任务上效果受限，且跨语言迁移能力未被系统验证。跨境电商、多语种客服等业务场景下，多语种语义类任务普遍存在小语种标注成本高、数据稀缺的痛点，亟需无需微调的轻量化跨语言任务适配方案。
### 方法关键点
- 基于因果中介分析筛选高贡献注意力头，从单语种few-shot样例的激活值中平均聚合得到任务FV，推理时直接注入LLM残差流实现任务引导，无需更新模型参数
- 设计两类零-shot验证场景：标准干净提示、带干扰标签的扰动提示，分别验证FV的性能增益和抗干扰能力
- 对比单/跨语言FV注入、FV+few-shot组合的效果，系统分析跨语言FV的相似度、最优头数、注入层数等配置的影响
### 关键结果
实验采用SemEval-2025 Task11的英/德/中/西/俄5种语言多标签情感分类数据集，在Qwen3-8B、Llama3.1-8B-Instruct上验证：
- 扰动零-shot场景下，注入跨语言FV后Qwen3-8B的中文情感分类Macro-F1从0提升至42.7，英文从0.6提升至50.2，平均提升超40个百分点
- 干净零-shot场景下，跨语言FV注入相比基线平均提升20+个百分点，跨语言FV与同语言FV效果差距小于2%
- 跨语言FV与few-shot结合可额外带来1-5个百分点的性能增益，无需目标语言标注即可达到接近同语言few-shot的效果
### 核心结论
不同语言提取的同任务FV在LLM隐空间相似度超过0.94，核心捕捉的是语言无关的任务级语义信号，而非语言特定的词汇模式
