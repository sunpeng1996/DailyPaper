---
title: 'Anamnesis: An Open-Source Platform for Large-Scale Backstory-Conditioned Survey
  Simulation'
title_zh: Anamnesis：基于背景故事约束的大规模调研仿真开源平台
authors:
- Song-Ze Yu
- Joseph Suh
- Serina Chang
- David M. Chan
affiliations:
- University of California, Berkeley
arxiv_id: '2607.10628'
url: https://arxiv.org/abs/2607.10628
pdf_url: https://arxiv.org/pdf/2607.10628
published: '2026-07-12'
collected: '2026-07-15'
category: LLM
direction: LLM 驱动的虚拟人群调研仿真
tags:
- LLM Simulation
- Persona Prompting
- Survey Emulation
- Open Source
- Demographic Control
one_liner: 用结构化背景故事约束LLM生成调研仿真结果，效果优于标准 persona 提示的开源平台
practical_value: '- 做用户偏好预研时可复用结构化叙事背景约束 persona 的prompt trick，比普通 persona 提示生成的偏好分布更贴合真实人群，降低小流量AB测的预研成本

  - 电商选品、营销文案预热测试可基于该框架快速生成不同 demographic 虚拟用户的反馈，无需提前招募真实用户采样，大幅降本提效

  - 用Agent模拟用户行为做推荐系统冷启动评估时，可借鉴probabilistic demographic resampling方法，快速生成覆盖不同用户群的测试样本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统真人调研成本高、响应率持续走低，触达特定 demographic 人群的落地难度大，现有基于标准 persona 提示的LLM仿真结果与真实人群意见分布偏差较大，无法满足调研需求。
### 方法关键点
1. 落地Anthology与Alterity框架，通过结构化叙事背景故事约束LLM响应，生成匹配特定人群特征的虚拟用户
2. 提供面向非技术用户的统一web交互界面，支持开放生成、概率人口重采样、多模态（图像/音频）调研能力
3. 完全开源，替代闭源商用仿真服务，支持透明可复现的调研实验
### 关键结果
两类场景验证效果均优于基线：① 复现Pew研究中心美国趋势面板的政治、生物医疗领域调研结果；② 模拟《纽约客》配文竞赛人类偏好，生成的意见分布与真实数据匹配度显著高于标准 persona 提示方案。
