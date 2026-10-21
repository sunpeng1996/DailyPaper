---
title: Evolving Agent Interfaces
title_zh: Agent S4：基于任务经验自主进化的计算机使用代理接口框架
authors:
- Saaket Agashe
- Yuzhe Yang
- Gonzalo Gonzalez-Pumariega
- Bhuvan Chandra Koduru
- Chih-Lun Li
- Jiachen Yang
- Ang Li
- Xin Eric Wang
affiliations:
- University of California, Santa Barbara
- Cornell University
- Carnegie Mellon University
- Simular
arxiv_id: '2610.28601'
url: https://arxiv.org/abs/2610.28601
pdf_url: https://arxiv.org/pdf/2610.28601
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 自主接口进化优化
tags:
- Computer-use Agent
- Interface Evolution
- Population-based Evolution
- Meta-agent
- LLM Agent
one_liner: 提出可自主进化接口的Agent S4，开源27B模型性能超GPT-5.5与Claude Opus且成本极低
practical_value: '- 可复用「Meta-agent分析任务轨迹→生成/优化工具接口→种群演化筛选」的框架，用于优化推荐/广告系统的Agent工具链，比如批量生成商品信息爬取、用户评论分析的专用API，降低人工开发工具的成本

  - 借鉴「合成无标注任务训练+独立验证集筛选」的演化范式，避免Agent工具过拟合到特定业务场景，提升工具在跨品类电商任务、多场景广告投放任务上的泛化性

  - 工程上可参考分层接口设计：系统级/应用级/跨应用级/任务级四级接口，针对电商场景定制商品操作、订单处理、用户服务等不同粒度的可复用Agent工具，提升任务执行效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机使用Agent的接口均由人工设计，存在三大痛点：一是接口迭代完全依赖人工分析任务轨迹、编写新原语，无法匹配快速增长的任务多样性与模型迭代速度；二是静态接口与任务不匹配时，Agent只能通过高成本的GUI试错执行弥补，效率极低且稳定性差；三是基于固定接口的技能蒸馏、流程复用等优化无法扩展接口能力边界，导致性能存在明显天花板。

### 方法关键点
- 双Agent架构：固定任务Agent执行合成任务生成无标注轨迹，Meta-agent仅基于轨迹分析即可迭代优化接口仓库，仓库包含可执行接口、使用说明、适用场景知识三类资产
- 种群演化策略：支持单仓库突变、双仓库交叉两种演化算子，通过独立验证集的任务表现筛选优质仓库，Meta-agent全程无法访问验证集数据，避免过拟合
- 分层接口设计：支持系统级、应用级、跨应用级、任务级四级接口扩展，可覆盖从通用操作到特定场景任务的全粒度需求

### 关键实验
在OSWorld V2 108项长周期桌面任务基准上，基于Qwen3.8-27B的Agent S4二进制成功率达21.3%，是同模型固定接口版本的3.8倍，超过GPT-5.5（13.0%）和Claude Opus 4.8（20.6%），单任务成本仅为二者的4.3%和1.5%；在ScienceBoard 169项科学任务基准上，同模型成功率从固定接口的41.4%提升至58.6%。

### 核心结论
自主进化接口是与模型迭代、Harness优化互补的Agent性能提升路径，仅靠接口进化即可让中小开源模型超过大参数闭源模型的表现，且成本低1-2个数量级。
