---
title: Cross-Domain Tracker Adaptation Without Target-Domain Labels via Vision-Language
  Agents
title_zh: 基于视觉语言Agent的无目标域标签跨域追踪器适配方法
authors:
- Daniel Davila
- Ravikumar Balakrishnan
- Mike Cochran
affiliations:
- Cisco Systems, Inc.
arxiv_id: '2609.05239'
url: https://arxiv.org/abs/2609.05239
pdf_url: https://arxiv.org/pdf/2609.05239
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: 多模态Agent · 无标注系统参数调优
tags:
- VLM
- Agent
- Cross-Domain Adaptation
- Hyperparameter Tuning
- Label-Free Optimization
one_liner: 用VLM诊断Agent实现无目标域标注的跨域追踪器自适应调优，性能优于传统无监督调优方法
practical_value: '- 电商新类目/新市场等缺标注的跨域推荐场景，可复用VLM Agent无标注调优思路，无需目标域标注即可迭代优化系统参数

  - 系统超参调优可替换黑盒贝叶斯优化方案，用Agent直接诊断业务bad case输出优化建议，避免调优降级原有优质配置

  - 调优流程新增分支逻辑：Agent未识别到明确失效模式时不修改配置，兼顾易迁移场景的性能稳定性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有跨域部署的检测追踪系统受域偏移影响性能下降，传统有监督超参迁移鲁棒性差，无标注贝叶斯优化在大域偏移场景下容易降级原有优质配置，人工调优效率低无法快速适配动态场景。
### 方法关键点
构建VLM诊断Agent迭代调优闭环：直接渲染追踪输出做视觉检查，识别失效模式并输出参数更新建议；新增选择性调优逻辑，无明确失效模式时不修改配置，保障易迁移场景性能稳定。
### 关键结果
MOT17→MOT20跨域场景下，有监督超参迁移导致HOTA从目标域上限0.357降至0.267，该方法无目标域标注即可追回67.8%的性能损失，仅比目标域上限低0.029；最高密度序列下可追回86.7%性能损失，效果优于基于手工代理目标的无监督贝叶斯优化。
