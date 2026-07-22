---
title: 'Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence'
title_zh: Apple-π：面向物理定律对齐的实体智能视频推理基准
authors:
- Runmao Yao
- Kairui Hu
- Yukang Cao
- Ruisi Wang
- Shulin Tian
- Ziang Cao
- Weichen Fan
- Ziqi Huang
- Yuhao Dong
- Hao Li
affiliations:
- S-Lab, Nanyang Technological University
- The Chinese University of Hong Kong
arxiv_id: '2607.16401'
url: https://arxiv.org/abs/2607.16401
pdf_url: https://arxiv.org/pdf/2607.16401
published: '2026-07-16'
collected: '2026-07-22'
category: Eval
direction: 视频模型物理推理能力评测
tags:
- VideoModel
- Benchmark
- PhysicalIntelligence
- Evaluation
- Reasoning
one_liner: 首个锚定经典力学定律的视频模型物理推理基准，可定位推理错误阶段
practical_value: '- 混合「规则硬指标+MLLM主观打分」的分层评测框架，可直接迁移到电商商品短视频生成的合规性、物理合理性评测场景

  - 分感知/匹配/推导三阶段的错误定位方法，可复用在多模态Agent的全链路Debug，快速定位故障环节

  - 单任务无混淆/多任务泛化拆分的测试集构建思路，可借鉴优化业务A/B测试用例设计，减少无关变量干扰'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型被认为内置物理世界常识，但现有评测仅校验输出的视觉合理性，不验证推理过程是否符合物理定律，缺乏可解释的错误定位能力。
### 方法关键点
1. 构建Orchard数据集：含400条覆盖10类经典力学任务的视频，拆分单定律无混淆诊断任务、多定律泛化任务两类；
2. 三阶段评测协议：基于标注首帧信息，依次完成物理参数感知、适用定律匹配、结果推导，用chain-of-frames prompting将生成视频作为可观测推理轨迹；
3. 混合评测套件：结合物理定律对齐的客观指标（位置、速度误差等）+ MLLM主观打分，可定位推理链路的错误阶段。
### 关键结果
11款主流视频模型测试最高分仅0.473，暴露感知→公式匹配→推导全链路瓶颈、多定律状态迁移能力弱、Sim-to-Real gap明显三大问题。
