---
title: Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized
  Language-Action Dual Bootstrapping
title_zh: 面向导航的策略同步语言-动作双自举递归自优化框架
authors:
- Songze Li
- Haoming Gu
- Ziyang Gong
- Zhitong Wang
- Gengze Zhou
- Zun Wang
- Yuhan Zhu
- Tianxiang Jiang
- Juanzi Li
- Qi Wu
affiliations:
- Fudan University
- Shanghai AI Laboratory
- Harbin Institute of Technology
- Shanghai Jiao Tong University
- Tsinghua University
arxiv_id: '2610.15782'
url: https://arxiv.org/abs/2610.15782
pdf_url: https://arxiv.org/pdf/2610.15782
published: '2026-10-10'
collected: '2026-10-15'
category: Agent
direction: 具身导航Agent · 递归自优化
tags:
- EmbodiedAgent
- SelfImprovement
- VisionLanguageNavigation
- Bootstrapping
- DataCentric
one_liner: 单模型统一导航、指令生成与空间理解，通过策略同步双自举实现无标注轨迹下的自提升
practical_value: '- 双任务联合优化架构可复用：对需要指令理解+内容生成的场景（如电商导购Agent的需求理解与话术生成），可采用单模型共享参数+任务prompt区分的方案，降低多模型维护成本的同时双向提升效果

  - 小批量策略同步更新逻辑可迁移：做Agent自优化时无需等待全量无标注数据处理完成再更新模型，拆分为小shard处理后立即更新，可保证生成的训练数据与当前策略对齐，避免监督滞后问题

  - 生成数据质量评估方法可复用：不要仅依赖BLEU、ROUGE等文本相似度指标评估生成内容质量，需加入下游任务执行验证（如导购话术生成后用实际点击/转化效果过滤），生成数据的下游效用更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉语言导航（VLN）方法要么采用分离的导航、指令生成模型，要么用固定模型标注全量轨迹后再更新，导致生成的监督信号与演进中的策略不匹配；同时人工标注成本极高，难以规模化扩展。

### 方法关键点
- 单模型统一三大能力：基于Qwen3.5-9B，用不同任务prompt区分导航（语言→动作）、指令生成（视觉/动作→语言）、空间理解三类任务，共享全部参数，无需额外输出头
- 策略同步双自举流程：将无标注轨迹拆分为小shard，每轮用当前模型为shard生成指令，再执行指令验证是否能高效到达目标，仅保留达标（终点距目标<3m且SPL达标）的样本，立即更新模型再处理下一个shard，保证监督与当前策略对齐
- 多任务联合训练：每轮更新同时混入空间理解数据，强化空间推理能力反哺导航效果

### 关键实验
在R2R-CE、RxR-CE导航基准及4个空间理解基准上测试，对比DualVLN、AwareVLN等SOTA：R2R-CE SR达68.6%、SPL达58.6%，RxR-CE SR达72.4%、nDTW达70.6%，相较冷启动版本SR分别提升15.7pct、17.7pct，同时空间理解能力也有小幅提升。

### 最值得记住的一句话
生成式监督的价值不取决于其和人类标注的文本相似度，而取决于其指导下游任务执行的实际效用。
