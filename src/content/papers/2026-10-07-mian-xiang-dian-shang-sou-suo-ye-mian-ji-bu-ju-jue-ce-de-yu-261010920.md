---
title: Language Models for Page-Level Layout Decisions in E-commerce Search
title_zh: 面向电商搜索页面级布局决策的语言模型研究
authors:
- Varun Joshi
- Eva C. Song
- ChengXiang Zhai
affiliations:
- Walmart Global Tech
- University of Illinois at Urbana-Champaign
arxiv_id: '2610.10920'
url: https://arxiv.org/abs/2610.10920
pdf_url: https://arxiv.org/pdf/2610.10920
published: '2026-10-07'
collected: '2026-10-09'
category: RecSys
direction: 电商搜索 · 页面布局离线评估
tags:
- E-commerce Search
- Page Layout Evaluation
- LLM-as-Judge
- Representation Learning
- Recommender Systems
one_liner: 对比三类语言模型方法实现电商搜索页次级模块插入决策离线评估，验证表征类方法效果最优
practical_value: '- 布局效果评估可优先选轻量预训练文本编码器（如ModernBERT）生成页面上下文表征+浅层分类器的方案，ROC-AUC比prompt-based方法高18%，成本远低于在线A/B测试

  - 次级模块插入的标签构造可复用论文的过滤规则：仅保留用户明确看到模块后的ATC行为（模块内点击/模块下方主商品ATC），大幅降低标注噪声

  - 若采用prompt分解打分方案，不要直接用LLM输出的等权综合结果，需用历史行为数据训练分类器重排各维度权重（如重复度、流中断成本权重需单独调优）

  - 表征方案无需额外拼接位置、模块类型等显式特征，编码器已自动编码相关信号，可减少特征工程工作量'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索页除主排序结果外，常插入次级推荐模块（如横向商品轮播），合适的插入策略可提升用户 engagement，反之则会干扰浏览；但现有页面布局评估依赖成本高昂的在线A/B测试，历史行为数据仅能覆盖已上线布局，无法评估未上线的候选方案，亟需可扩展的离线评估方法。

### 方法关键点
- 任务定义为二分类：判断在指定位置插入次级模块后，用户体验是否优于无模块基线，标签基于ATC行为构造，仅保留用户明确浏览过模块的样本，排除无有效行为的噪声数据
- 对比三类方案：1）直接prompt判断（含基础版DP和链式分解判别的PDJ，基于Mistral-7B-Instruct实现）；2）prompt派生特征分类（PFC）：将PDJ输出的6维度打分+位置、模块类型等显式特征输入分类器；3）表征-based方法（REC）：用ModernBERT编码页面上下文生成语义embedding，再接浅层神经网络分类

### 关键结果
基于Walmart 1周1.1万条搜索流量样本（8:2拆分训练测试集，正负样本平衡）实验：
- REC-Snn的ROC-AUC达0.853，比最优prompt-based方法PDJ高0.18，比最优PFC方法高0.113
- 直接prompt的DP方案全预测正样本，AUC仅0.596；PFC去掉显式特征后AUC下降0.02-0.05，而REC加显式特征无明显收益

**最值得记住的结论**：电商页面布局的离线评估核心是识别与历史用户行为相关的语义模式，轻量语义表征方案的效果和效率均显著优于基于prompt推理的方案。
