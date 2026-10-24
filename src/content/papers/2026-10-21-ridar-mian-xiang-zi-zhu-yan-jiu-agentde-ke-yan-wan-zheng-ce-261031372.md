---
title: 'RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated
  Detection and Runtime Intervention'
title_zh: RIDAR：面向自主研究Agent的科研完整性检测与干预框架
authors:
- Jiening Siow
- Amy Xin
- Junjie Wang
- Ziyu Tang
- Zijun Yao
- Yunjia Qi
- Fanjin Zhang
- Lei Hou
- Jie Tang
- Juanzi Li
affiliations:
- Tsinghua University
- Renmin University of China
- Zhipu AI
arxiv_id: '2610.31372'
url: https://arxiv.org/abs/2610.31372
pdf_url: https://arxiv.org/pdf/2610.31372
published: '2026-10-21'
collected: '2026-10-24'
category: Agent
direction: 自主Agent 合规检测与运行时干预
tags:
- Autonomous Agent
- Runtime Intervention
- Compliance Detection
- LLM Agent
- Trajectory Audit
one_liner: 提出覆盖14类科研完整性违规的RIDAR框架，支持事后检测与运行时干预，降低Agent任务违规残留
practical_value: '- 可复用「全流程违规分类体系+事后检测+运行时干预」架构，落地到电商业务Agent（如智能选品、内容生成Agent）的合规管控，规避虚假宣传、数据造假等违规

  - 长轨迹Agent的违规检测思路可迁移到推荐系统用户/商品行为审计场景，批量识别异常操作轨迹

  - 运行时动态修正逻辑可嵌入现有Agent工作流，无需重构全链路即可降低违规残留，工程落地成本低'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM驱动的自主研究Agent已覆盖科研全流程，但长执行轨迹下易出现破坏研究有效性、可复现性的科研完整性违规（RIV），缺乏系统性检测与干预方案。
### 方法关键点
1. 构建覆盖科研全生命周期的RIVT分类体系，包含14类RIV；
2. 开发RIDAR-post-hoc事后检测框架，基于分类体系识别Agent轨迹中的违规；
3. 推出RIDAR-runtime运行时干预框架，在Agent执行过程中动态检测并修正违规。
### 关键结果
RIDAR-post-hoc在60条专家标注的RIV-Gold基准上F1达85.2%；对覆盖50个任务的300条野生Agent轨迹的RIV-Wild数据集检测显示，99.7%的轨迹存在违规，共识别3964个违规实例；RIDAR-runtime可将任务完成后残留的RIV降低36.8%。
