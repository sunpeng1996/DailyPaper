---
title: 'HalluTracer: Hallucination Detection via Depth-Averaging Truth Signals'
title_zh: HalluTracer：基于深度平均真值信号的幻觉检测方法
authors:
- Zhihao Guo
- Zonghan Wu
- Huan Huo
- DaYong Ye
- Junwei Zhang
- Weiran Yao
- Zhiwei Liu
- Qingsong Wen
- Yilei Shao
affiliations:
- East China Normal University
- University of Technology Sydney
- City University of Macau
- Meta
- Microsoft AI
arxiv_id: '2608.16353'
url: https://arxiv.org/abs/2608.16353
pdf_url: https://arxiv.org/pdf/2608.16353
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: LLM可靠性 · 预解码幻觉检测
tags:
- Hallucination Detection
- White-box Probe
- Transformer Interpretability
- Pre-decoding Detection
- LLM Reliability
one_liner: 通过聚合Transformer全层真值信号的预解码幻觉检测框架，性能优于同预算白盒基线
practical_value: '- 电商导购Agent、商品参数问答、推荐理由生成场景可接入该框架，在回答生成前就拦截幻觉信息（如虚假规格、错误活动规则），无需等待全句生成后校验，降低token成本的同时避免错误信息触达用户

  - 业务中用白盒LLM做生成类任务时，无需纠结选哪层hidden state做探针，直接对全层探针输出分数做平均即可得到更鲁棒的检测结果，比单层探针最高提升14个点AUROC

  - 针对长文本生成场景（如购物攻略、商品测评），仅提取prompt最后一个token的各层表征做检测即可达到最优效果，不需要对全prompt做池化，进一步降低计算量

  - 若推理资源有限，仅采集前8层信号做平均就能拿到接近全层的检测效果，可灵活平衡性能与开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有幻觉检测方案要么是黑盒后校验，需要多次采样生成消耗大量推理成本；要么是白盒单层探针，依赖最优层选择泛化性差，且丢弃了Transformer前向过程中跨层分布的真值信号，无法满足高可靠LLM应用（如电商客服、Agent）的低开销实时检测需求。

### 方法关键点
- 定位prompt末尾的回答起始位置token，提取其在Transformer每一层的隐藏表征，为每层训练专属线性探针输出真值logit，形成跨层logit轨迹，可在生成任何回答token前完成信号采集
- 几何分析验证不同层探针方向近正交、信号弱相关，直接对全层logit取平均即可抑制层噪声，无需复杂权重分配，且Fisher恒等式证明该平均策略接近最优线性聚合效果
- 仅将平均后的单标量输入逻辑回归分类器完成幻觉判定，推理开销极低

### 关键结果
覆盖6个开源LLM（LLaMA2-7B、LLaMA3.1-8B、Qwen2.5 7B~72B）、5个幻觉基准数据集，对比同预算白盒基线（Fact-Probe、ITI-Probe、IRIS），AUROC提升1~14个百分点；在Agent专用幻觉基准上，最高获得11.7个百分点的AUROC提升；仅采样8层信号即可达到接近全层的检测效果。

最值得记住的结论：LLM的事实性信号是跨层逐步迭代构建的，而非局限在某单一层，简单的全层信号平均就能充分挖掘表征中的判别信息，无需复杂的层选择或权重优化。
