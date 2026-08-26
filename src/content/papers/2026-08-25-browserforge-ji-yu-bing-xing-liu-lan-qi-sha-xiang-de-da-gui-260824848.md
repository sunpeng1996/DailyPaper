---
title: 'BrowserForge: Scaling Web Episode via Parallel Browser Sandboxes'
title_zh: BrowserForge：基于并行浏览器沙箱的大规模网页交互轨迹生成框架
authors:
- Fei Tang
- Huawen Shen
- Zhiqiong Lu
- Zhengxi Lu
- Pengyuan Lyu
- Chengquan Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
- Tencent LLM Department
arxiv_id: '2608.24848'
url: https://arxiv.org/abs/2608.24848
pdf_url: https://arxiv.org/pdf/2608.24848
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Web Agent · 大规模交互轨迹自动合成
tags:
- Web Agent
- GUI Agent
- Trajectory Synthesis
- Multimodal LLM
- Parallel Computing
one_liner: 通过并行浏览器沙箱从公开网页生成20万+跨站轨迹，大幅提升纯GUI Web Agent性能
practical_value: '- 搭建电商/广告自动化Web Agent时，可复用并行浏览器沙箱集群架构，自主生成大规模跨站交互训练数据，无需局限于固定站点列表，大幅降低人工标注成本

  - Proposer-Solver双Agent生成任务+规则+大模型校验+统一CoT改写的清洗pipeline，可直接迁移到自有Agent训练数据生产流程，有效提升数据质量

  - 业务侧落地纯GUI Agent可优先提升站点覆盖多样性，而非单纯堆叠同站轨迹数量，小模型在多样本下的性能增益超过大模型零样本，适合低成本落地

  - 轨迹设计中0-1000归一化坐标、统一动作空间的定义，可直接复用在GUI交互类Agent的训练推理接口，降低不同分辨率适配成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
纯GUI Web Agent避免了依赖HTML/可访问树的脆弱性和高Token成本，但现有训练轨迹数据集站点覆盖窄、数量少，自动合成方案也局限于固定站点列表，无法适配开放Web场景的泛化需求，亟需低成本生成大规模、高多样性交互轨迹的方案。

### 方法关键点
- 公开网页URL sourcing：从Common Crawl采样URL，经过可达性、内容、黑名单、IP可用性四层过滤，获得数十万可访问站点
- 并行浏览器沙箱集群：共享任务队列调度300+并发沙箱，高利用率生成页面渲染结果，支持多分辨率、多UA、多语言配置提升多样性
- Proposer-Solver双Agent合成：Proposer基于页面信息生成3个候选任务后筛选最优可执行任务，Solver通过计划-行动-反思-校验闭环执行任务，生成原始轨迹
- 轨迹清洗：规则过滤（正常终止）+大模型校验（任务完成）+统一CoT改写，去除噪声，标准化推理格式

### 关键结果
生成203238条来自不同站点的轨迹，训练Qwen3.5-4B/9B模型，在Online-Mind2Web基准上成功率从25.66%提升到33.33%（+7.67），9B模型从29.33%提升到38%（+9.33）；Multimodal-Mind2Web平均步骤准确率从38.2%提升到43.8%，性能随数据量单调增长无饱和。

**最值得记住的一句话**：开放Web本身就是最大最便宜的训练数据源，站点覆盖多样性对Web Agent泛化性能的提升远超过同规模固定站点轨迹。
