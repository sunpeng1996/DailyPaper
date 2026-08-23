---
title: Scaling Manual-Grounded Appliance Manipulation with Data Synthesis and Unified
  Planning
title_zh: 基于手册指引的家电操作规模化实现：数据合成与统一规划
authors:
- Yuxing Long
- Lei Kang
- Ziyan Yu
- Yuzheng Gao
- Bin Cheng
- Jiyao Zhang
- Xiaoqi Li
- Haolin Yang
- Dongjiang Li
- Hui Shen
affiliations:
- 北京大学
- 北京航空航天大学
- 京东科技信息技术有限公司
arxiv_id: '2608.15863'
url: https://arxiv.org/abs/2608.15863
pdf_url: https://arxiv.org/pdf/2608.15863
published: '2026-08-16'
collected: '2026-08-23'
category: Agent
direction: 具身Agent 家电操作长时序规划优化
tags:
- Embodied Agent
- Data Synthesis
- Long-Horizon Planning
- Domain Dataset
- Hierarchical Graph
one_liner: 提出MAGE数据合成管道与家电操作数据集UseAppliance，训练7B规划模型性能超基线10倍
practical_value: '- 家电类电商的智能客服、上门安装/维修指导场景，可复用MAGE的层级图+手册数据合成思路，自动生成操作指引、故障排查话术，大幅降低人工标注成本

  - 垂直领域Agent长时序任务规划场景，可参考「领域手册+层级结构图合成训练数据」的范式，快速低成本搭建领域专属规划能力

  - 垂直场景小参数LLM落地可参考该方案：用高质量垂直数据集训练7B级小模型即可远超通用大模型表现，显著降低推理部署成本'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有大模型无法适配家电操作所需的长时序、状态依赖、抗干扰规划能力，核心瓶颈是缺乏面向任务的多样化标注数据集。
### 方法关键点
1. 提出MAGE可扩展数据合成管道，引入**Hierarchical Appliance Graph (HAG)**，从家电手册自动生成部件对齐、长时序规划、闭环恢复三类标注数据；
2. 基于MAGE构建首个大规模家电操作规划数据集UseAppliance，覆盖22类家电，含89K+部件标注、53K+操作任务、33K+闭环调整步骤；
3. 基于该数据集训练7B参数端到端规划模型AppliancePlan。
### 关键结果
在RealAppliance-Bench上开环规划性能超最优基线10倍以上，全任务表现优于现有SOTA；6类家电真机实验验证sim-to-real迁移效果优异。
