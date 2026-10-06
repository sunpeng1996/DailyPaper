---
title: Self-Supervised Scaling of Terminal Environments for Scientific Domains
title_zh: 面向科学领域的终端Agent环境自监督扩展方法
authors:
- Zhongzhi Li
- Yucheng Shi
- Zongxia Li
- Junyao Yang
- Ruhan Wang
- Yu Wang
- Jingyuan Huang
- Jichao Yu
- Ninghao Liu
- Haitao Mi
affiliations:
- Tencent HY LLM Frontier
- University of Georgia
- University of Maryland, College Park
- National University of Singapore
- Hong Kong Polytechnic University
arxiv_id: '2610.02710'
url: https://arxiv.org/abs/2610.02710
pdf_url: https://arxiv.org/pdf/2610.02710
published: '2026-10-01'
collected: '2026-10-06'
category: Agent
direction: 终端Agent · 训练环境自监督构建
tags:
- Terminal Agent
- Self-Supervised Learning
- SFT
- Verifier
- Workflow Reconstruction
one_liner: 提出软件在环重建框架，复用现有工作流低成本构建科学域终端Agent训练环境与验证器
practical_value: '- 可复用「现有业务工作流作为标注源」的思路：电商规则引擎、推荐链路现有服务可直接生成训练样本与验证目标，无需单独编写标注规则，大幅降低垂直域Agent训练数据成本

  - 分层验证器设计可直接迁移：结构合法性+领域语义校验+反捷径检查的三层结构，适合电商客服、运营工具类Agent的输出正确性校验，避免仅校验格式忽略业务语义的问题

  - 公共/隐藏用例拆分的评估范式：训练时提供公开输入输出样例、评估用未见过的隐藏用例，可直接用于电商内部工具Agent、运营自动化Agent的能力验收，避免过拟合已知场景'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前终端Agent训练环境大多聚焦软件工程领域，科学、工业等垂直领域落地面临两大核心痛点：一是每个任务都需要单独开发领域专用验证器，定制化开发成本极高；二是现有任务构造方式无法规模化扩展，垂直域高质量训练数据严重不足，限制终端Agent在专业场景的落地效果。

### 方法关键点
- 提出软件在环重建自监督框架：复用现有可执行业务工作流作为基准，对同一工作流生成多组输入配置，拆分为公开输入输出样例（供Agent学习）与隐藏验证集（用于最终校验）
- 分层语义验证器：整合结构合法性校验、领域专属语义比对、反捷径检查三层规则，支持数值容差、格式等价等灵活判断，避免字节完全匹配的假阴性和仅结构校验的假阳性
- 高质量轨迹筛选SFT：仅保留通过隐藏集全量验证的Agent交互轨迹作为SFT数据，支持过采样增强训练效果

### 关键实验结果
- 构建SWR数据集，覆盖6个科学领域、46个软件家族、500个工作流、3000个任务；Qwen3.8-Max三次尝试可解决27.9%的任务，生成1422条验证通过的高质量轨迹
- 用3000条采样轨迹对Qwen3.8-27B做SFT，Terminal-Bench 2得分从47.94%提升至53.56%，在TB2、TB4、LHTB、SWR100四个基准上均超过4个同token量的对比训练语料

**最值得记住的一句话：现有可执行业务系统本身就是最高质量的Agent训练标注源与验证器，无需从零构建任务规则**
