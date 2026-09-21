---
title: 'CIBuzzBench: A Benchmark for Cross-Lingual Understanding of Chinese Internet
  Buzzwords'
title_zh: CIBuzzBench：中文网络热词跨语言理解基准数据集
authors:
- Yifan Wang
- Junyu Lu
- Qifan Wang
- Shun Zhang
- Chaozhuo Li
- Jiahao Liu
- Zhijun Cao
- Lingbin Bu
- Fanliang Bu
affiliations:
- People’s Public Security University of China
- Dalian University of Technology
- Meta AI
- Beijing University of Posts and Telecommunications
- Meituan
arxiv_id: '2609.21722'
url: https://arxiv.org/abs/2609.21722
pdf_url: https://arxiv.org/pdf/2609.21722
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: 多语言LLM评测 · 网络热词理解
tags:
- Cross-lingual-LLM
- Benchmark
- Internet-Buzzword
- Safety-Evaluation
- Multilingual-LLM
one_liner: 构建首个中英跨语言中文网络热词理解基准，含3001条标注样本与三类评估任务
practical_value: '- 跨境电商、出海内容推荐场景的内容审核模块，可直接复用该基准的热词标注库补充中文网络黑话、谐音梗的跨语言映射规则，降低有害内容漏审率

  - 多语言Agent、跨语言搜索推荐的意图理解模块，可使用该基准的三类任务做预上线评测，校验文化相关语义的理解准确率

  - 跨语言营销文案生成、商品介绍翻译场景的LLM微调，可加入该数据集的热词-英文对应样本做LoRA微调，减少文化梗翻译偏差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

## 动机
现有中文网络热词研究仅覆盖单语中文理解场景，缺乏跨语言到英文的评测基准，而这类根植于本土文化的非字面热词（含谐音、暗语类有害内容）的跨语言理解能力，是多语言LLM、跨境内容安全系统的核心刚需。
## 方法关键点
构建首个中英跨语言中文网络热词理解基准CIBuzzBench，包含3001条经过标注的中文网络热词，标注信息覆盖英文释义、英文对等词、分类标签、有害性标签，设计三类评测任务：含义解释、跨语言对等词匹配、文化关联有害性检测，覆盖中英文prompt两种评测设置。
## 关键结果
当前主流商用/中文LLM在该基准上表现不佳：非字面语义细粒度解释准确率较单语场景低40%以上，扰动选项下匹配准确率不足30%，有害性检测校准误差超25%，文化类语义跨语言迁移仍是显著短板。
