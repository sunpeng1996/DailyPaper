---
title: 'Compass: Continuously Aligning Social Media Feeds via In-Situ Reflections'
title_zh: Compass：通过原位反馈持续对齐社交媒体信息流与用户反思性偏好
authors:
- Aadit Barua
- Leijie Wang
- Amy X. Zhang
affiliations:
- The University of Texas at Austin
- University of Washington
arxiv_id: '2608.04274'
url: https://arxiv.org/abs/2608.04274
pdf_url: https://arxiv.org/pdf/2608.04274
published: '2026-08-04'
collected: '2026-08-06'
category: RecSys
direction: 信息流推荐 · 用户偏好持续对齐
tags:
- Recommender-Systems
- User-Preference-Alignment
- In-situ-Interaction
- Short-Form-Video
- Lightweight-Intervention
one_liner: 通过浏览中原位轻量交互与模拟行为信号，持续对齐短视频信息流与用户长期偏好
practical_value: '- 无需改造现有推荐系统底层的上层干预方案：通过模拟用户观看/点赞/搜索行为引导黑盒推荐算法输出，叠加客户端DOM操作直接增删内容，可快速落地到短视频/电商feed定向优化场景

  - 偏好采集的原位轻量交互设计：捕捉用户浏览中的行为信号（如短视频划走、商品快速滑过）触发低干扰偏好询问，比独立配置页的用户参与度提升2个数量级，可复用在电商个性化推荐的偏好迭代场景

  - 短内容多模态语义匹配的轻量化方案：取预加载队列的短视频元数据+3张关键帧调用低延迟多模态LLM生成语义描述，嵌入后和用户偏好做相似度匹配，兼顾实时性和准确率，可复用在短视频商品、短内容feed的实时过滤场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有社交媒体信息流推荐以即时 engagement（点击、观看时长、点赞）为优化目标，往往偏离用户经反思后的长期偏好（如减少无效娱乐、增加知识类内容摄入）。现有偏好对齐方案多为一次性配置、需要用户跳转独立设置页操作，使用门槛高、易被遗忘，无法适配偏好演化与推荐算法的自然漂移，实际使用率极低。

### 方法关键点
- 以YouTube Shorts浏览器插件形式实现，无需改造平台底层推荐系统，核心包含三大模块：实时多模态视频处理管线、可演化偏好表示模块、双层feed对齐模块
- 实时管线拦截平台预加载的视频请求，提取元数据+3张自动关键帧，调用低延迟多模态LLM生成统一语义描述并 embedding，平衡处理速度与准确性
- 偏好采用动态rubric表示，基于主动学习不确定性采样，对相似度接近阈值的内容弹出原位轻量询问，收集反馈迭代偏好模型
- 对齐模块监控48小时滑动窗口内偏好内容占比，低于阈值时后台模拟用户搜索、观看、点赞行为引导底层推荐算法；同时直接操作DOM增删内容，保证用户即时看到对齐效果

### 关键实验
10天的受控用户实验（N=15），对比需手动配置触发对齐的基线方案：Compass组人均偏好修改次数11.5次vs基线0.14次；符合用户偏好的内容占比49.3%vs20.3%；对应内容观看时长占比58.7%vs21.0%；两组SUS易用性得分分别为84.1、83.2，无显著差异，未破坏 casual 浏览体验。

### 核心结论
所有需要用户主动参与的推荐调控功能，必须完全嵌入日常浏览流程，不能要求用户跳出当前场景付出额外努力。
