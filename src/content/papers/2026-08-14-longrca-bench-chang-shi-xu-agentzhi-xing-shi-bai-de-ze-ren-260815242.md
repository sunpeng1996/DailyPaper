---
title: 'LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon
  Agent Failures'
title_zh: LongRCA Bench：长时序Agent执行失败的责任归因与根因定位基准
authors:
- Yunfei Zhang
- Boyu Feng
- Changhua Pei
- Zexin Wang
- Zhihuang Peng
- Xinlong Liu
- Hengyue Jiang
- Difeng Ma
- Jiayi Zhang
- Yongzhou Yao
affiliations:
- 中国科学院计算机网络信息中心
- 重庆大学
- 新加坡管理大学
- 阿里巴巴通义实验室
- 清华大学
arxiv_id: '2608.15242'
url: https://arxiv.org/abs/2608.15242
pdf_url: https://arxiv.org/pdf/2608.15242
published: '2026-08-14'
collected: '2026-08-26'
category: Agent
direction: Agent长时序执行失败归因基准与方法
tags:
- Agent
- Failure Attribution
- Root Cause Localization
- Long Horizon
- Benchmark
one_liner: 构建含1140条真实长失败轨迹的诊断基准，提出免训练RCTA方法大幅提升归因准确率
practical_value: '- 多角色电商导购Agent、复杂用户路径转化归因等长路径场景，可复用RCTA的「分段摘要+回溯handoff指令」思路，无需全量输入长上下文，大幅降低诊断的token开销

  - 多Agent协作的推荐/广告系统线上故障排查，可参考LongRCA的标注规则：将责任角色与根因步骤分开评估，避免把执行错误的下游角色错判为责任方

  - 业务侧多Agent系统灰度迭代评估，可借鉴LongRCA的基准构建思路：自动收集真实失败轨迹标注核心归因标签，无需人工注入错误，更贴合线上实际故障分布'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序LLM Agent执行失败后，仅靠结果级评估只能得到失败结论，无法定位最早引入决定性错误的步骤和对应责任角色，现有失败归因基准多针对短轨迹，无法支撑数百步长序列的诊断需求，大幅提升了Agent系统的排障和迭代成本。

### 方法关键点
- 构建LongRCA Bench：收集软件修复、旅行规划、网页交互等5个领域共1140条真实非人工注入的失败轨迹，平均长度156.3步，中位数145步，最长728步，每条独立标注责任角色、最早决定性根因步骤和标注理由，根因到最终失败的中位数间隔达48步
- 提出免训练RCTA方法：先按规则将长轨迹分段，每段生成摘要召回候选错误步骤，再将候选回溯到更早的handoff指令，区分是指令本身带错还是执行层引入新错误，独立输出责任角色和根因步骤，无需额外训练

### 关键结果
统一使用DeepSeek-V4-Flash作为backbone，对比全量输入提示、逐步扫描、ECHO等5种现有基线方法：RCTA的责任角色准确率达51.1%，根因步骤精确准确率24.1%，±5步准确率37.4%，较最强基线ECHO分别提升23.6、10.9、12.7个百分点。

> 最值得记住：长时序Agent失败归因需将责任角色与根因步骤作为独立目标评估，不能直接从根因步骤的发布方推导责任归属，避免错判上游规划错误的责任方。
