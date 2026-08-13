---
title: 'Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill'
title_zh: Spark-to-Paper：基于可组合技能的端到端学术论文生成系统
authors:
- Zhuoyang Qian
- Biao Wu
- Yiran Wang
- Chris D Yan
- Desan Dai
- Liangwei Zheng
- Jin Jiang
- Junsheng Zhang
- Wenhao Wang
affiliations:
- Vast Intelligence Lab
- University of Technology Sydney
arxiv_id: '2608.11924'
url: https://arxiv.org/abs/2608.11924
pdf_url: https://arxiv.org/pdf/2608.11924
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent 技能化编排 · 自动化科研
tags:
- LLM Agent
- Skill Orchestration
- Automated Research
- Self-Critique
- Deterministic Check
one_liner: 将端到端论文生成拆解为13个可组合技能嵌入编码助手，无需独立Agent编排服务
practical_value: '- 落地复杂Agent系统时可复用「可组合技能+现有工具原生能力」的轻量架构，无需从零搭建独立编排服务、存储中间件，大幅降低开发运维成本，适合电商/推荐场景的文案生成、报表自动化等任务

  - 采用「LLM做决策判断+确定性脚本做规则校验」的分工模式，在推荐的商品文案生成、广告创意审核等场景可大幅减少幻觉，保证输出符合业务规则

  - 长流程任务可复用「提前预设目标+结果校验修订+循环熔断」的设计，比如推荐系统的自动A/B实验报告生成、全链路营销方案生成，避免无效迭代，同时杜绝事后凑指标的问题

  - 分层自评审机制（局部自检+全局对抗评审）可迁移到Agent的输出质量管控，比如推荐的搜索query改写、商品标题生成的效果校验，提升审核准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自动化科研Agent均为独立系统，需要额外编排服务与基础设施，和日常科研的编码环境割裂，仅能覆盖部分科研流程，同时存在引用伪造、结论不可靠、生成图表不可编辑等问题，亟需轻量、高可靠的端到端论文生成方案。

### 方法关键点
- 拆分为13个可组合技能，全部嵌入现有编码助手，通过共享项目目录的 artifacts 通信，无需独立编排层
- 模型判断与确定性操作分离：LLM负责推理决策，脚本执行可校验操作（引用校验、LaTeX编译、数据绘图等）
- 实验规划与报告分离：提前预设所需证据，实验结果产出后再修订论文结论，避免结果篡改
- 确定性校验门+分层自评审（本地自审+全局对抗评审），同时设置7次循环上限熔断自反驳死循环，失败轨迹留存为报告而非强行输出成功结论
- 角色感知的图表生成：实验结果图直接从数据代码生成，解释性图先生成栅格再用代码重构为可编辑矢量图

### 关键结果
在8个受控科研主题上测试，对比人类预印本、AI Scientist等现有系统、单轮LLM草稿基线：引用有效性99.5%，图表可编辑率96.4%，虚假声明检测率从单轮的14%提升到全链路的92%，对抗评审精度74%，单篇平均成本$8.1，耗时3.2小时，Token消耗11.9M。

最值得记住的一句话：自动化任务系统不应该强制每个目标都成功，用可校验的规则兜底、给失败路径设置熔断边界，比强行追求高完成度更重要。
