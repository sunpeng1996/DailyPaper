---
title: NeuroCogMap Reveals Cognitive Organization of Large Language Models
title_zh: NeuroCogMap：揭示大语言模型的认知组织结构
authors:
- Zhongxiang Sun
- Haolang Lu
- Qiang Ma
- Qi Li
- Qipeng Wang
- Liang Pang
- Chenyu Liu
- Qiankun Li
- Hao Sun
- Kun Wang
affiliations:
- 中国人民大学高瓴人工智能学院
- 北京邮电大学
- 香港大学
- 中国科学院自动化研究所
- 华中科技大学
arxiv_id: '2607.00397'
url: https://arxiv.org/abs/2607.00397
pdf_url: https://arxiv.org/pdf/2607.00397
published: '2026-06-30'
collected: '2026-07-15'
category: LLM
direction: 大语言模型可解释性 · 认知功能映射
tags:
- LLM Interpretability
- Cognitive Neuroscience
- Hallucination Detection
- Functional Mapping
- Model Alignment
one_liner: 受认知神经科学启发的NeuroCogMap框架，可定位LLM功能分区、解释错误并关联人类认知
practical_value: '- 可复用LLM错误的内部签名检测思路，对推荐/Agent场景下的幻觉、输出偏差做快速定位拦截，降低业务badcase

  - 借鉴功能分区映射方法，定向干预LLM在商品介绍、营销文案生成时的错误模块，提升生成内容准确率

  - 可利用框架的认知层级匹配思路，优化电商场景下用户query理解的语义对齐效果，提升搜索/推荐相关性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有研究无法解释LLM类认知行为背后的内部表征系统，难以关联其表现、错误与人类认知的对应关系，缺乏系统级的LLM功能组织解析框架。
### 方法关键点
受认知神经科学启发的NeuroCogMap框架，将LLM内部特征划分为独立功能分区，关联可解释功能、认知能力与认知层级，建立跨模型部分守恒的稳定功能组织映射。
### 关键结果
可准确定位幻觉、偏见、拒绝失效、谄媚四类主流LLM错误对应的表征与行为控制系统扰动，为错误检测与定向干预提供内部签名；对人类自然语言理解的皮层反应预测效果显著提升，高阶联合皮层匹配度最优；可挖掘隐藏策略优化人类决策经典模型。
