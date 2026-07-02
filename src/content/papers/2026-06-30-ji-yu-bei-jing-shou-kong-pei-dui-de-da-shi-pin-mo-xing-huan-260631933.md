---
title: 'No Place to Hide: Benchmarking Video Hallucination with Background-Controlled
  Pairs'
title_zh: 基于背景受控配对的大视频模型幻觉评估基准
authors:
- Haojian Huang
- Harold Haodong Chen
- Meng Luo
- Junjia Du
- Shanqing Xu
- Ziheng Chen
- Yanxiang Huang
- Yinchuan Li
- Ying-Cong Chen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Knowin AI
- National University of Singapore
- Nanyang Technological University
- Huazhong University of Science and Technology
arxiv_id: '2606.31933'
url: https://arxiv.org/abs/2606.31933
pdf_url: https://arxiv.org/pdf/2606.31933
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: 大视频模型 · 幻觉评估基准
tags:
- Video Hallucination
- LVM
- Evaluation Benchmark
- Controlled Dataset
- Video QA
one_liner: 构造背景相似前景语义不同的视频对基准，精准定位大视频模型的真实幻觉错误
practical_value: '- 多模态内容理解评测可复用「固定背景+差异前景」的配对构造方法，排除无关干扰，精准定位模型缺陷，适用于电商短视频理解、广告内容审核等场景的模型评测

  - 可复用PairFlow流水线，用文生图/文生视频工具批量生成受控测试集，大幅降低人工标注成本，可快速构造推荐/广告场景的专项测试集

  - 评估多模态Agent的视频理解能力时，可直接引入VidPair-Halluc的细粒度时空QA范式，提升幻觉问题的检测准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有大视频模型(LVM)幻觉评估基准多依赖文本扰动或对抗问题，未控制视觉背景一致性，无法区分模型错误来自真实幻觉还是背景差异，难以精准定位能力短板。
### 方法关键点
提出PairFlow流水线，借助文生图、文生视频技术批量构造背景高度相似、前景语义存在明显差异的对抗视频对，覆盖时空推理10个语义维度，构建受控评估基准VidPair-Halluc。
### 关键结果数字
基准包含1K组高质量对抗视频对、11K个受控背景/前景变量的时空问答对；在主流LVM上测试发现，模型在对抗场景下的细粒度视频鲁棒理解能力普遍存在明显短板。
