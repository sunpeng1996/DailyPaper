---
title: 'CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension'
title_zh: CaRGo-T：因果推理思维图提升多模态幽默理解性能
authors:
- Abhilash Nandy
- Rahul Seetharaman
- Aman Bansal
- Rounak Saha
- Manav Nitin Kapadnis
- Millon Madhur Das
- Pawan Goyal
- Niloy Ganguly
affiliations:
- Microsoft Research India
- LinkedIn, USA
- Nutanix, USA
- Indian Institute of Science, India
- Apple, USA
arxiv_id: '2608.23172'
url: https://arxiv.org/abs/2608.23172
pdf_url: https://arxiv.org/pdf/2608.23172
published: '2026-08-23'
collected: '2026-08-28'
category: Reasoning
direction: 多模态推理 · 因果思维图
tags:
- Causal Reasoning
- Graph-of-Thought
- Multimodal
- VLM
- Humor Comprehension
one_liner: 提出将多模态幽默因果关系序列化为代码结构的Graph-of-Thought框架，提升VLM幽默理解性能
practical_value: '- 广告/内容创意幽默度识别场景，可借鉴因果图序列化思路，将图+文案的实体、语义关联编码为轻量结构，提升梗类、meme类创意的点击率预判准确率

  - 复杂多模态理解任务中，可将思维图序列化为VLM易解析的代码格式，零样本/小样本场景下效果优于线性CoT推理，适配内容审核、创意质量打分等需求

  - 做VLM/LLM Prompt工程时，可加入因果关联结构化思考要求，无需微调即可获得1%+效果提升，落地成本极低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前VLMs在多模态幽默理解上表现较差，幽默依赖跨模态实体、事件、上下文的隐式关联，常规Prompt或线性Chain-of-Thought难以捕捉复杂推理链。
### 方法关键点
1. 提出CaRGo-T推理框架，将多模态幽默背后的因果、上下文关系构建为轻量图结构
2. 由VLM将该图序列化为代码格式表示，可被同/异VLM解析，适配零样本、上下文学习场景
### 关键结果
在4个涵盖讽刺、反讽、meme的数据集上测试，对比现有推理基线：
- 幽默理解任务准确率提升1~20%
- 幽默检测任务准确率提升1~3%
- 互信息分析显示CaRGo-T生成的推理表示比基线包含更多和目标输出相关的有效信息
