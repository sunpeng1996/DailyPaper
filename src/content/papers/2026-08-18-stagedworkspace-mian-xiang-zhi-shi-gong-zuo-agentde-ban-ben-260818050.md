---
title: 'StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents'
title_zh: StagedWorkspace：面向知识工作Agent的版本管控工作空间
authors:
- Yining Hua
- Hongbin Na
- Yifan Zhou
- Akshay Kalose
- Cyrus Ayubcha
- Levi Lian
affiliations:
- Harvard University
- Raycaster AI
- University of Technology Sydney
- University of Washington
- Stanford University
arxiv_id: '2608.18050'
url: https://arxiv.org/abs/2608.18050
pdf_url: https://arxiv.org/pdf/2608.18050
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: 知识工作Agent 版本管控工作空间优化
tags:
- Agent
- Knowledge_Work
- Version_Control
- Workspace
- RAG
one_liner: 提出带版本同步的原生+解析双视图工作空间，解决知识工作Agent多视图版本漂移问题
practical_value: '- 搭建电商运营/商品治理类Agent时，可复用「原生文件+解析缓存双视图+内容哈希校验同步」架构，避免检索到旧版商品参数、活动规则，导致生成的运营文案、活动配置出错

  - 涉及多格式文件（商品Excel表、活动PDF、素材文档）处理的Agent流程，可加入格式感知的编辑Diff预览能力，让Agent提交前校验修改内容，实测可提升2.5~8.5分的任务得分，降低人工审核成本

  - 动态更新的电商知识库RAG系统，可借鉴哈希键缓存失效机制，仅重新解析修改过的文件，无需全量重索引，降低更新开销同时避免返回过时商品/活动信息'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前知识工作Agent处理代码、文档、表格等多格式工件时，检索用的解析视图、编辑的原生文件、提交的最终版本常出现版本漂移，导致检索到旧信息、编辑与参考源不一致，现有方案仅覆盖代码场景，非编码的办公混合文件场景缺乏明确的状态同步契约。

### 方法关键点
- 设计三态工作空间：权威原生文件$W_t$、带源路径和内容哈希标签的解析缓存$C_t$、初始态到当前态的变更Diff$\Delta_t$，三者通过内容哈希绑定同步
- 哈希键同步机制：每次编辑后扫描文件哈希，仅标记哈希变化的解析记录为stale，异步重解析变更文件，无需全量更新
- 支持格式感知的Diff预览：文本用行Diff、表格用单元格级Diff、二进制文件用前后预览，Agent提交前可查看变更
- Agent执行时每次工具调用批量操作后自动同步三态，保证所有操作基于同一版本状态

### 关键实验
在OFFICEQA PRO（PDF问答基准）和APEX-AGENTS（跨格式专业工作基准）上做ablation：双视图比仅原生模式提升OfficeQA Pass@1 8.3~12.1个点，比仅解析模式提升APEX平均rubric得分4.7~9.2个点；完整SW-AGENT用Gemini 3.1 Pro在OfficeQA上达到63.9% Pass@1，比同模型公开基线高34.6个点；开启Diff预览后文件编辑任务得分提升2.5~8.5个点，且性能提升不伴随显著成本上升。

### 核心结论
知识工作Agent的性能差距很多时候不是模型能力不足，而是工作空间状态不同步导致的，弱模型通过合理的状态同步设计可以大幅缩小和强模型的表现差距
