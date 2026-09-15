---
title: Towards Evolving Context Parameterization for Large Language Models
title_zh: 大语言模型动态演化场景下的上下文参数化方法PLUME
authors:
- Xiaobing Shi
- Zherui Li
- Yiming Jiang
- Kun Wang
- Yufei Guo
affiliations:
- Nanyang Technological University
- Peking University
arxiv_id: '2609.14168'
url: https://arxiv.org/abs/2609.14168
pdf_url: https://arxiv.org/pdf/2609.14168
published: '2026-09-12'
collected: '2026-09-15'
category: LLM
direction: LLM 上下文参数化 · 动态更新优化
tags:
- Context Parameterization
- LoRA
- Continual Update
- Knowledge Editing
- Benchmark
one_liner: 提出无训练的PLUME方法，解决上下文参数化持续更新冲突，在MUSE基准上大幅领先基线
practical_value: '- 电商导购Agent、用户长期记忆场景可复用PLUME架构：将用户历史交互、商品动态信息参数化为LoRA，结合query激活的最新局部信息做自适应解码，相比RAG减少长上下文重复处理开销，无需重训即可适配信息更新

  - 商品、活动信息频繁更新的推荐/广告场景，可借鉴「新旧LoRA差异放大」思路：对更新部分对应的参数偏移做加权增强，既保证最新信息生效，又保留无关历史信息的参数状态，避免全量重训成本

  - 已落地Doc-to-LoRA做上下文内化的业务，可直接叠加PLUME的自适应解码模块：根据全局、局部LoRA预测的JS divergence动态加权，无需改动原有LoRA生成逻辑，即可解决新旧信息冲突问题，改造成本极低

  - 可复用MUSE-Bench的构建思路，构造业务专属的动态信息评测集：明确区分更新影响、不影响的query，验证上下文内化方案在信息迭代场景下的正确性和鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有上下文参数化方法（如Doc-to-LoRA、Context Distillation）均假设上下文静态，无法适配Agent、电商等场景下信息持续更新的需求，新旧信息混杂会导致模型依赖过期信息、输出结果不一致；而RAG、长上下文方案又存在重复处理的高推理开销，亟需适配动态演化场景的低成本上下文参数化方案。
### 方法关键点
- 定义MUSE（Memory Updating with Sequential Evolution）任务，构建包含5个数据集、3k+上下文、13k+QA对的MUSE-Bench，同时评测更新融入能力和未受影响信息的保留能力
- 提出无训练的PLUME方法：首先用预训练Doc-to-LoRA分别生成更新前后全量上下文的LoRA权重，构造全局更新表示，放大最新更新带来的参数偏移；再根据query词汇相关性+时序优先级激活局部记忆证据，生成对应的LoRA作为局部视图；解码阶段基于全局、局部预测的JS divergence动态计算权重，自适应融合两者的log概率输出
### 关键实验结果
在Qwen3、Gemma2两个基座上对比Doc-to-LoRA、Context Distillation、AnyEdit等基线，平均ROUGE-L Recall相对提升29.9%，LLM-as-a-Judge相对提升54.9%；未受影响信息保留率（Locality）比Doc-to-LoRA高10.25个点，更新效率和D2L持平，仅生成阶段有少量额外开销。
### 核心结论
上下文参数化的动态更新场景中，有效信息大多仍保留在模型输出分布中仅排序被压低，无需训练、仅通过全局更新增强+局部证据激活的融合方式即可大幅提升效果
