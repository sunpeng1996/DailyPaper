---
title: 'SplatLab: Autonomous Scientific Discovery for 3DGS Research'
title_zh: SplatLab：面向3D高斯泼溅（3DGS）研究的自主科学发现系统
authors:
- Seemandhar Jain
- Manmohan Chandraker
affiliations:
- University of California San Diego
arxiv_id: '2610.30468'
url: https://arxiv.org/abs/2610.30468
pdf_url: https://arxiv.org/pdf/2610.30468
published: '2026-10-20'
collected: '2026-10-25'
category: Agent
direction: 自主科研Agent · 3D领域任务自动化
tags:
- Autonomous Agent
- Scientific Discovery
- 3D Gaussian Splatting
- LLM Agent
- Auto Optimization
one_liner: 提出面向3DGS领域的端到端自主研究Agent，可自动完成基线复现、方案优化、生成可溯源研究成果
practical_value: '- 可复用「验证过的基线插件库+变异迭代」设计模式，降低推荐/广告算法迭代的重复开发成本，例如排序模型优化时基于成熟基线做插件化修改

  - 可迁移级联加权Elo锦标赛+ falsifier淘汰机制，用于多候选召回/排序策略的自动评估筛选，快速选出效果最优的策略

  - 可借鉴「所有指标绑定可溯源实验日志」的设计，解决算法迭代中效果复现难、归因难的问题，尤其是AB实验的全链路溯源'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
3DGS领域论文复现需数周专家工程投入，现有自主科研系统存在模板短、可执行性差、溯源弱的问题，暂无在活跃CV子领域落地的端到端方案。
### 方法关键点
5项核心设计：① 基于已验证的基线复现骨架做插件变异生成候选方案；② 跨8个island的级联加权Elo锦标赛，结合GPU实测PSNR与文本梯度反馈打分；③ 常设falsifier模块对失败方案扣Elo分，将压力测试通过率纳入筛选；④ 所有报告指标绑定训练日志，无支撑数据时流程不终止；⑤ 7类3DGS分类体系封装EVOLVE-BLOCK标记，实现跨代码库的领域适配。
### 关键结果
生成的方案PSNR较复现基线高0.18~3.78dB，其中星云渲染场景提3.78dB（无此前3DGS方案）；研究周期从数月人力压缩至数天自动计算
