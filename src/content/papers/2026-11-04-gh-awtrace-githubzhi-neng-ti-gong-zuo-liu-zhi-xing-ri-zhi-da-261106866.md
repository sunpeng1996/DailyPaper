---
title: 'GH-AWTrace: A Large-Scale Dataset of GitHub Agentic Workflow Execution Logs'
title_zh: GH-AWTrace：GitHub智能体工作流执行日志大规模数据集
authors:
- Jasem Khelifi
- Hao Li
- Ali Ouni
- Mohammed Sayagh
- Mohamed Aymen Saied
affiliations:
- ÉTS Montreal, University of Quebec
- Queen's University
- Laval University
arxiv_id: '2611.06866'
url: https://arxiv.org/abs/2611.06866
pdf_url: https://arxiv.org/pdf/2611.06866
published: '2026-11-04'
collected: '2026-11-16'
category: Agent
direction: Agent 智能体工作流执行日志公开数据集
tags:
- Agentic Workflow
- Execution Trace
- Dataset
- GitHub
- Failure Analysis
- Multi-Agent
one_liner: 公开覆盖2.5万条GitHub智能体工作流的411万次运行、56万条非空执行日志的关联数据集
practical_value: '- 做电商/广告领域自动化Agent（比如商品审核、工单处理、报表生成）的团队，可参考数据集里的Agent故障重试、权限适配、工具调用fallback模式，优化业务Agent的执行稳定性

  - 多Agent协作场景（比如电商客服多技能坐席Agent分配、内容审核多维度校验）可复用数据集里的任务分发、超时兜底、多数投票结果聚合的设计逻辑

  - 搭建Agent可观测系统时，可直接参考该数据集的「工作流配置-运行元数据-执行日志」三级关联schema，降低trace系统的设计成本

  - 训练Agent故障分类、异常检测模型时，可直接使用该公开数据集的真实执行日志，无需自行爬取脱敏生产数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有智能体工作流相关研究仅关注配置定义与最终运行结果，缺失执行过程中的工具调用、权限拦截、故障重试、多Agent协作等中间行为数据；同时GitHub对公开工作流的日志有留存时效限制（执行日志最多保留90天，运行记录最多保留400天），历史执行证据易丢失，无法支撑Agent执行行为的深度分析与优化。
### 方法关键点
- 采用分段文件大小搜索策略绕过GitHub API单查询最多返回1000条结果的限制，仅保留YAML头部包含固定生成标记的有效工作流配置，避免误匹配
- 全量拉取有效工作流对应时段的所有运行元数据，通过仓库ID、文件路径实现工作流与运行记录的关联
- 采集保留期内的所有执行日志，校验ZIP包完整性，建立「仓库-工作流-运行-日志」三级关联schema，支持多表关联查询与回溯
### 关键结果
- 数据集覆盖5051个GitHub仓库的25014条验证通过的智能体工作流，对应4112526条运行记录，562877份非空执行日志，总大小56.1GB
- 统计得出31.7%的非空日志对应运行失败，失败原因涵盖权限拦截、服务提供商认证失败、工具调用拒绝等多类场景
- 覆盖18种运行触发场景，其中定时触发占日志总量的44.89%，是最常见的工作流触发方式
### 核心结论
仅靠工作流定义和最终运行结论无法还原Agent的真实执行行为，执行过程的trace数据是分析Agent故障、优化Agent决策逻辑的核心依据
