---
title: 'Beyond Accuracy: What Language-Subspace Interventions Capture, Remove, and
  Improve'
title_zh: 超越准确率：语言子空间干预的捕获效果、信息残留与优化权衡
authors:
- Shaanil Punglia
- Dadhichi Telwadkar
- Vaibhav Rathore
- Siddharth Sureka
- Neha Bhargava
affiliations:
- Motilal Oswal Financial Services, India
- Indian Institute of Technology Bombay, India
arxiv_id: '2611.05278'
url: https://arxiv.org/abs/2611.05278
pdf_url: https://arxiv.org/pdf/2611.05278
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: 多语言LLM激活干预 · 性能权衡分析
tags:
- Multilingual-LLM
- Activation-Steering
- Subspace-Intervention
- Causal-Interpretability
- Reasoning
one_liner: 揭示语言子空间干预的语言信息残留问题与准确率-输出语言保真度的权衡
practical_value: '- 做跨语种推荐/多语言Agent时，不能仅评估核心任务准确率，必须新增输出语言保真度指标，避免用户收到非目标语言内容影响体验

  - 激活干预的实际收益需警惕prompt语言偏置混淆，可通过仅修改示例语言的对照实验，确认收益来自干预本身还是模型进入高资源语言推理模式

  - 轻量低秩（如rank 1）的子空间干预往往比强擦除操作综合收益更高，做LLM推理优化时可优先尝试窄范围编辑，避免破坏多语言控制相关分布式特征'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言LLM的语言子空间干预方法常以准确率提升为唯一评价标准，忽略了干预可能导致输出语言漂移的问题，也未验证子空间是否真的完全覆盖语言信息，存在机制解释和实际落地的漏洞。

### 方法关键点
- 对比两种子空间构建方法：基于多语言激活均值的MEAN-SVD、基于同问题翻译激活差的DIFFPCA，对照无语言标签的ACTIVATION-PCA和随机子空间
- 采用冻结探针/重训练探针双维度验证子空间擦除后语言信息的残留情况
- 提出联合准确率指标：要求答案正确且输出为问题原语言，同时设置仅修改示例/提示语言的对照组，分离干预收益与prompt偏置的影响

### 关键实验
在MATH、MGSM多语言数学推理数据集上对4款7-9B开源模型测试：1. rank10的MEAN-SVD/DIFFPCA仅能捕获24%~46.2%的翻译相关激活变异；2. 擦除子空间后重训练探针仍能以99.7%以上的准确率分类语言，语言信息未被完全消除；3. 准确率最高的干预方案使语言保真度下降19.24个百分点，仅rank1 MEAN-SVD投影方案实现1.6个百分点的联合准确率提升；4. 仅修改prompt示例为英语/中文即可复现相当的准确率提升，同时伴随64%~95%的语言保真度下降。

最值得记住的结论：多语言场景下的模型干预不能仅以核心任务准确率为评价标准，必须同时验证输出是否符合用户预期的语言等约束，避免所谓的性能提升其实是改变了原本的任务契约。
