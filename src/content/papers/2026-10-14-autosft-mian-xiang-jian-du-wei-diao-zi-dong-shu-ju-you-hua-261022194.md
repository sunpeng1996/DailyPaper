---
title: 'AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning'
title_zh: AutoSFT：面向监督微调自动数据优化的多Agent系统
authors:
- Bingxiang He
- Pengqi Sun
- Shihao Peng
- Shaoxuan Li
- Huiyu Xiao
- Hongjian Shi
- Zixuan Fu
- Ziqing Qiao
- Yuxin Zuo
- Cheng Qian
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
- ModelBest Inc.
- University of Illinois Urbana-Champaign
- The Chinese University of Hong Kong
arxiv_id: '2610.22194'
url: https://arxiv.org/abs/2610.22194
pdf_url: https://arxiv.org/pdf/2610.22194
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 多Agent协作 · LLM 微调数据自动优化
tags:
- Multi-Agent
- SFT
- Data Curation
- Instruction Tuning
- Code Generation
one_liner: 提出执行-分析-合成拆分的多Agent架构，实现SFT数据全流程自动优化，效果远超单Agent方案
practical_value: '- 做LLM4Rec的SFT数据迭代时，可直接复用多Agent拆分架构：用独立执行Agent处理训练、评估等脏活，节省主Agent上下文，避免历史信息丢失

  - 优化推荐场景的Instruction tuning数据时，可引入4个互补分析Agent（训练数据质检/ bad case分析/ 训练信号归因/ 历史尝试沉淀），避免单视角优化陷入局部最优

  - 当现有数据池覆盖不到长尾推荐场景（比如小众类目query理解）时，可复用自带验证器的合成子Agent，自动生成符合约束的训练样本，填补数据缺口

  - 做任何数据迭代闭环时，都可遵循"每轮从base模型重训"的对照方法，精准归因每个数据改动的收益，排除混淆变量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单Agent做SFT数据优化时，仅能完成单一的数据比例调整动作，且上下文被训练、评估的冗余日志占满，频繁丢失历史信息，远达不到人类数据工程师可实现的剪枝、修复、替换、合成等全链路操作效果，数据优化收益天花板低。

### 方法关键点
- 定义6类SFT数据操作空间：比例调整、样本剪枝、样本修复、重标注、新样本合成、顺序调整
- 采用多Agent拆分架构：元Agent统筹全局，执行子Agent独立处理训练、转换、评估全流程，仅返回结果文件路径，不占用元Agent上下文；4个分析子Agent分别从训练数据质量、bad case、训练动态、历史尝试四个互补视角输出数据优化建议；合成子Agent针对现有数据池覆盖不足的能力点，自动生成带验证的新样本
- 每轮迭代都从base模型重训，严格控制训练参数、token预算等变量，确保每个改动的收益可精准归因

### 关键实验
- 指令微调场景：base模型为Qwen3-1.7B，对比单Agent baseline，执行子Agent让上下文压缩次数减半，分析子Agent让IFEval指标提升+6.5，加合成子Agent后IFEval再涨+3.4、IFBench涨+2.9
- 代码生成场景：对比无优化的单Agent，加分析子Agent后MBPP+提升+3.7，加合成子Agent后仅用6轮就达到和15轮分析组相当的效果

### 核心结论
自动化SFT数据优化的瓶颈，不在于单个动作的强度，而在于系统架构能否覆盖人类数据工程师的全链路操作空间，多Agent角色拆分是实现这一点的低成本可行方案
