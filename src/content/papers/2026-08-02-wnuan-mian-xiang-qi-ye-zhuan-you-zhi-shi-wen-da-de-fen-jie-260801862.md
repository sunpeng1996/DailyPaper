---
title: 'Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise
  Knowledge'
title_zh: Wnuan：面向企业专有知识问答的分阶段后训练方案
authors:
- Xiaofeng Shi
- Xiaosong Qiu
- Wenxin Ma
- Qian Kou
- Yiming Pan
- Longbin Yu
- Ying Liu
- Haiping Wang
- Hua Zhou
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
- Beijing District Heating Group Co., Ltd. (BDHG)
- Beijing University of Posts and Telecommunications (BUPT)
arxiv_id: '2608.01862'
url: https://arxiv.org/abs/2608.01862
pdf_url: https://arxiv.org/pdf/2608.01862
published: '2026-08-02'
collected: '2026-08-05'
category: Training
direction: 大模型后训练 · 企业知识问答适配
tags:
- Post-Training
- Enterprise QA
- SFT
- Reinforcement Learning
- Domain Adaptation
one_liner: 提出三阶段后训练流程，提升企业专有知识问答效果同时可控通用能力损失
practical_value: '- 做电商/企业垂直领域Agent、客服LLM适配时，可复用三阶段流程：从私有文档构造任务监督数据→带通用数据回放的SFT→基于残差错误的RL微调，平衡领域效果和通用能力留存

  - 微调采样时优先选择模型回答错误的残差样本，可比随机采样/全量池采样提升近3个点的准确率，大幅降低微调数据成本

  - 领域适配后通用指令跟随能力会小幅下降，业务上线前需单独评估通用交互场景的效果损耗，必要时补充通用指令样本回放'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
企业专有知识问答场景需要大模型适配未出现在公开预训练语料的内部政策、流程等知识，同时尽量保留通用能力，现有方案难以同时兼顾领域效果、训练成本与通用能力留存。
### 方法关键点
提出三阶段后训练pipeline：1）从私有文档自动构造任务导向的监督数据集；2）混合通用数据回放执行SFT，缓解灾难性遗忘；3）针对SFT阶段的残差错误样本做RL微调，低成本优化剩余bad case。
### 关键结果
在707题的WnuanBench上，32B模型可接受回答率(AAR)从适配前52.76%提升至SFT后80.06%，RL后达91.51%；残差错误采样比全量池/尺寸匹配随机采样分别高3.11/2.97个点AAR；适配后通用基准平均得分仅下降5.17分，损失集中在指令跟随场景；自动评估集成与领域专家判断一致性达90.5%。
