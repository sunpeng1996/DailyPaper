---
title: 'JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models'
title_zh: JoyNexus：面向服务的多租户视觉-语言-动作模型后训练框架
authors:
- Haoran Sun
- Wentao Zhang
- Junyang Hua
- Hedan Yang
- Yongjian Guo
- Yifei Zhang
- Xiaolong Xiang
- Mingxi Luo
- Jing Long
- Chen Zhao
affiliations:
- JDT AI Infra
- Peking University
- Beihang University
- Beijing Institute of Technology
- Tsinghua University
arxiv_id: '2607.16074'
url: https://arxiv.org/abs/2607.16074
pdf_url: https://arxiv.org/pdf/2607.16074
published: '2026-07-16'
collected: '2026-07-22'
category: Training
direction: 多租户大模型训练资源调度优化
tags:
- VLA
- Multi-Tenant
- Post-Training
- Group Batching
- Resource Scheduling
one_liner: 提出面向VLA模型的多租户后训练服务，通过资源调度与共享提升GPU利用率降低租户成本
practical_value: '- 多租户LLM/VLA训练服务可参考其服务解耦架构，拆分训练、推理、环境服务通过API暴露，大幅降低业务侧基础设施适配成本

  - 多租户共享底座模型训练场景可复用group batching技巧，对前缀兼容的异构数据合并前向传播，有效降低总GPU耗时

  - 存在大量bursty小批量训练需求的业务（如多品类小样本SFT、多Agent策略微调）可参考其调度与租户隔离机制，平衡资源利用率与数据安全'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型后训练的算力服务普遍采用单租户独占GPU/CPU资源模式，既要求租户额外适配基础设施，短周期、突发类workload成本极高，也导致服务商的资源利用率低下。
### 方法关键点
1. 架构解耦为Training Model Service、Inference Model Service、Environment Service三类模块，基于共享底座模型+租户专属插槽对外提供API，租户可直接调用高层语义API，也可基于底层API自定义算法；
2. 全局训练/推理队列统一调度多租户任务，租户的动作模块、优化器、训练数据、策略版本完全隔离；
3. 引入group batching机制，对前缀兼容的异构VLA数据合并处理，共享主干网络前向传播过程。
### 关键结果
对比单租户独立执行模式，JoyNexus通过跨租户资源调度，显著减少总GPU耗时，提升服务整体资源利用率。
