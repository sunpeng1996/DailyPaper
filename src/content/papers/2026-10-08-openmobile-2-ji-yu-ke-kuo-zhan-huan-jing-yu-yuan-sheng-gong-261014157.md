---
title: 'OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments
  and App-Native Tools'
title_zh: OpenMobile-2：基于可扩展环境与原生工具的通用移动Agent框架
authors:
- Chenyang Yan
- Yingying Zhang
- Kanzhi Cheng
- Qiushi Sun
- Zhengyuan Pan
- Zheng Ma
- Hang Yan
- Yian Wang
- Nuo Chen
- Jialin Cao
affiliations:
- Nanjing University
- SenseTime
- The University of Hong Kong
- Xi'an Jiaotong University
- National University of Singapore
arxiv_id: '2610.14157'
url: https://arxiv.org/abs/2610.14157
pdf_url: https://arxiv.org/pdf/2610.14157
published: '2026-10-08'
collected: '2026-10-19'
category: Agent
direction: 移动Agent · 混合GUI-原生工具交互
tags:
- Mobile Agent
- GUI Agent
- Hybrid Tool Use
- Open Dataset
- Reinforcement Learning
one_liner: 开源110+App的移动Agent训练环境、12K轨迹数据与混合GUI-工具交互框架
practical_value: '- 电商App端自动化Agent可借鉴混合GUI+原生工具设计：将高频操作（商品搜索、加购、订单查询等）封装为App原生工具，相比纯GUI点击减少交互步骤，提升任务成功率与执行效率

  - 通用GUI Agent训练固定数据预算时，优先扩大覆盖App品类而非堆同品类数据，可显著提升跨域泛化能力

  - 可复用SFT+环境内RL的训练范式：先用专家演示轨迹做SFT，再用可自动校验的环境任务做RL微调，可进一步提升真实设备迁移性能

  - 行业Agent benchmark可参考MobileGym++设计：基于业务状态而非截图/轨迹做校验，判断任务完成更准确，还支持同一任务下不同交互模式的公平对比'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有移动Agent训练存在三大核心痛点：开源环境覆盖商业App少，真实App环境难重置、并行训练成本高；高质量交互轨迹多为闭源，开源数据规模小、场景单一；纯GUI交互效率低、鲁棒性差，现有混合工具方案多为外挂工具，未与App原生状态打通，无法实现无缝交互。

### 方法关键点
- 构建MobileGym++训练环境：包含35个高保真模拟商业App+62个安卓模拟器App，共110+App，支持跨App工作流、一键重置、业务状态自动校验，覆盖电商、出行、金融等7个领域
- 开源OpenMobile-Data-v2数据集：包含11.6K标注交互轨迹（含1.7K混合GUI-工具轨迹）、2K+可执行RL任务（自带自动reward校验逻辑）
- 提出混合GUI-App原生工具交互范式：在50+App中封装300+原生工具，Agent可在同一任务中交替使用GUI点击和工具调用，共享同一App底层状态
- 训练流程：先用轨迹数据做SFT，再基于环境可校验任务做RL微调，同时支持纯GUI和混合模式训练

### 关键结果数字
27B版本在AndroidWorld基准达79.9，MobileWorld基准达50.4，真实设备SPA-Bench基准达59.6，较基线Qwen3.6-27B提升27.7分，性能超过多数开源移动Agent；混合模式较纯GUI模式在MobileGym++基准上成功率提升10.3分，交互步骤减少5.8步；固定2K轨迹数据预算下，训练覆盖App从15个提升到53个，跨未知App任务成功率提升6.8分。

最值得记住的一句话：移动Agent性能提升的核心抓手是环境覆盖度的扩大，混合GUI+原生工具的交互范式是兼顾灵活性和效率的可行路径。
