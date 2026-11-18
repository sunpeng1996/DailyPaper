---
title: 'COTTI: Contrastive Training and Time-Aware Inference for Robust Industrial
  Recommendation under Promotional Drift'
title_zh: COTTI：促销漂移下鲁棒工业推荐的对比训练与时序感知推理
authors:
- Maolei Huang
- Jing Tian
- Dexuan Duan
- Fangfang Lin
- Huawei Cao
- Shuhan Song
affiliations:
- Alibaba Group
- University of Chinese Academy of Sciences
- Santa Clara University
arxiv_id: '2611.22597'
url: https://arxiv.org/abs/2611.22597
pdf_url: https://arxiv.org/pdf/2611.22597
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 电商促销场景推荐鲁棒性优化
tags:
- Distribution Shift
- Contrastive Learning
- CVR Prediction
- Time-aware Inference
- E-commerce Recommendation
one_liner: 通过跨周期对比、样本重加权与时序推理缓解促销场景推荐性能衰减
practical_value: '- 促销场景可复用三阶段优化范式：训练期用跨周期对比对齐用户历史表征降低分布偏移影响，再通过历史兴趣距离重加权促销样本权重，推理期固定模型参数仅调整logit，避免全量重训成本

  - 推理侧ABA模块可直接迁移到节日/大促等已知时间节点场景：用dropout蒙特卡洛采样估计预测不确定性，结合提前公布的活动时间高斯核做logit单向修正，实测仅增加2.2ms
  p99延迟，换3%+ CVR增益性价比高

  - 注意权衡全局指标与新品类探索：重加权机制会小幅降低新品类付费商品召回，若业务重点是拉新/破圈可降低RW权重系数γrw，或单独为新品类样本设置权重下限'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
电商大促等促销活动会导致流量结构、用户购买行为、转化率分布发生剧烈漂移，常规训练的推荐模型适配慢，存在CVR预估不准、排序效果下降的问题；过往方法要么仅做训练侧数据重加权，要么无法兼顾历史偏好稳定性与促销期需求变化，还普遍需要全量模型更新，难以适配短周期大促场景。

### 方法关键点
- 跨周期对比对齐（CPC）：将用户常规期、促销期历史行为作为正样本对做自适应加权InfoNCE损失，用户两类行为差异越大，对齐权重越低，避免强制统一偏好抑制促销期跨品类需求
- 主动重加权（RW）：计算促销样本的商品表征与用户常规期兴趣表征的距离，指数函数动态调整样本权重，低于平均距离的样本权重>1，高于的<1，降低低意图探索行为的干扰
- 自适应边界对齐（ABA）：推理期不更新模型参数，用M次dropout前向传播的logit方差作为不确定性代理，结合促销活动时间的高斯核函数，单向修正logit，缓解促销期CVR普遍低估问题

### 关键实验
在飞猪多月份含618、双11的流量数据集上训练，离线对比Base、HDR、TEN等SOTA基线，COTTI离线AUC达0.8127，比TEN高0.0026；10天线上A/B对比生产HDR模型，CVR相对提升3.14%，RPM提升2.68%；推理侧ABA模块仅增加2.2ms p99延迟，吞吐量从15400降至14700 req/s，性能损耗可控；但RW机制会让新品类付费商品召回下降0.08个百分点。

最值得记住的一句话：促销场景的推荐优化需要兼顾历史偏好稳定性、短期变化适配性与部署成本，三阶段分离的设计比端到端全量重训的性价比更高。
